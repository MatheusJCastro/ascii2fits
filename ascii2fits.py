#!/usr/bin/env python3

############################################################
# Transform an ASCII two column file into a FITS Spectrum  #
# Matheus J. Castro                                        #
# v1.2                                                     #
# Last Modification: 01/27/2023                            #
# Contact: matheusdejesuscastro@gmail.com                  #
############################################################

# to run the code, provide two arguments:
# Name of the folder for the program search for ascii files
# Name of the extension to search for
# Example: ./ascii_to_fits.py folder_name .txt

# The first column must be wavelength values
# And the second one, flux values
# By default, the code skips the first two lines of the file, be aware of that

from astropy.io import fits
import numpy as np
import pathlib
import sys

dir_name = sys.argv[1]  # get the directory name passed
ext = sys.argv[2]  # get the desired extension to transform
path = pathlib.Path(dir_name)  # transform it in a path
fl_names = list(path.rglob("*"+ext))  # get all the ascii files with the extension ext

# print the total number of files to be created
leng = len(fl_names)
print("Files to be created: ", leng)

for i in range(len(fl_names)):
    fl_name = fl_names[i]
    fl1 = np.loadtxt(fl_name, skiprows=2)

    crval1 = fl1[0][0]  # get the first wavelength value
    cdelt1 = float(fl1[1][0] - crval1)  # calculate the wavelength step

    hdu = fits.PrimaryHDU(fl1.T[1])  # create the Primary HDU of the fits with flux values
    hdu.header["CRVAL1"] = crval1  # add to the header the first wavelength value
    hdu.header["CDELT1"] = float("{:.5f}".format(cdelt1))  # add to the header the wavelength step

    hdul = fits.HDUList([hdu])
    hdul.writeto(str(fl_name)+".fits", overwrite=True)  # save the spectrum

    # print the progress in steps of 10 files only
    if i % 10 == 0:
        print("Progress {} out of {}.".format(i, leng), end="\r")
print("")
