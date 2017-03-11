#!/usr/bin/env python

from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import glob


ext_modules = [ ]
ext_modules += [Extension("quicklook.primitives.matutils", 
                         ['code/primitives/matutils.pyx'],
                         extra_compile_args=['-fopenmp'],
                         extra_link_args=['-fopenmp'],
                      )]

ext_modules += [Extension("quicklook.utr.fitramp", 
                          ['code/utr/fitramp.pyx'],
                          extra_compile_args=['-fopenmp'],
                          extra_link_args=['-fopenmp'],
                      )]


setup(    
    name='quicklook', 
    packages = {'quicklook', 'quicklook.primitives', 'quicklook.utr', 'quicklook.image',
                'quicklook.parallel'},
    package_dir = {'quicklook': 'code', 'quicklook.primitives':'code/primitives',
                   'quicklook.image':'code/image', 'quicklook.utr':'code/utr',
                   'quicklook.parallel':'code/parallel'},
    data_files = [('quicklook/calibrations', ['code/calibrations/lowres/mask.fits',
                                           'code/calibrations/lowres/pixelflat.fits']),
                  ('quicklook/calibrations/lowres' + 
                                                  ['code/calibrations/lowres/lensletflat.fits',
                                                  'code/calibrations/lowres/lowres_tottrans.dat',
                                                  'code/calibrations/lowres/lamsol.dat']),
                  ('quicklook/calibrations/highres_J' + 
                                                  ['code/calibrations/highres_J/lensletflat.fits',
                                                  'code/calibrations/highres_J/J_tottrans.dat',
                                                  'code/calibrations/highres_J/lamsol.dat']),
                  ('quicklook/calibrations/highres_H' + 
                                                  ['code/calibrations/highres_H/lensletflat.fits',
                                                  'code/calibrations/highres_H/H_tottrans.dat',
                                                  'code/calibrations/highres_H/lamsol.dat']),
                  ('quicklook/calibrations/highres_K' + 
                                                  ['code/calibrations/highres_K/lensletflat.fits',
                                                  'code/calibrations/highres_K/K_tottrans.dat',
                                                  'code/calibrations/highres_K/lamsol.dat'])],
    install_requires = ['numpy', 'scipy', 'astropy'],
#     scripts=['scripts/buildcal', 'scripts/extractcube'],
    scripts=['scripts/quicklook'],
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
) 
