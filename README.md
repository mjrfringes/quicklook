# Quicklook

This program uses a frozen version of Tim Brandt's CHARIS data reduction pipeline from March 2017.

It is a watchdog that looks at a directory for new CHARIS data files being created. When a new file is created, it opens it and reads the EXPTIME keyword in the header, and wait that amount until the current exposure is finished. Once the exposure is finished, it determines whether the file is a monochromatic flat or a regular data to be reduced. 

If it is a monochromatic flat, quicklook calls the buildcal command and creates a new calibration folder in /home/mrclean/calibdir, with the date at which the data was taken.

If the new CHARIS files are not monochromatic flats, then quicklook calls an extraction script. It will use whichever calibration that is closest in time.

How to use it:

```
cd /home/mrclean/quicklook/
./quicklook_watchdog
```

This should automatically find the correct folder where the data is being stored. In case you want to run quicklook in a particular folder, you can specify a folder such as:

```
./quicklook_watchdog /home/data/charis/scratch
```

and it will monitor new files that are added in that folder.


# Call quicklook without the watchdog

The quicklook_watchdog script located in /home/mrclean/quicklook/ is just a watchdog bash script. It calls the following Python script:

```
./home/mrclean/quicklook/code/quicklook
```
which does all the heavy lifting. This script can be used independently to reduce data the following way:

```
./home/mrclean/quicklook/code/quicklook my_filename
```

This allows to bypass the wait times on the quicklook watchdog. The arguments can consist of any expression that can be parsed by Python's glob package, like:

```
./home/mrclean/quicklook/code/quicklook CRSA*.fits
```
