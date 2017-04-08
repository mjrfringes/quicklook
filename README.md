# Quicklook

This program uses a frozen version of Tim Brandt's CHARIS data reduction pipeline from March 2017.

It is a watchdog that looks at a directory for new CHARIS data files being created. When a new file is created, it opens it and reads the EXPTIME keyword in the header, and wait that amount until the current exposure is finished. Once the exposure is finished, it determines whether the file is a monochromatic flat or a regular data to be reduced. 

If it is a monochromatic flat, quicklook calls the buildcal command and creates a new calibration folder in /home/mrclean/calibdir, with the date at which the data was taken.

If the new CHARIS files are not monochromatic flats, then quicklook calls an extraction script. It will use whichever calibration that is closest in time.

How to use it:

```
cd /home/mrclean/quicklook/
./quicklook
```
