# ASCII2FITS

*Written by: Matheus J. Castro*  
*Under MIT License*  

## Objevtive

This program will convert your ASCII two columns table files into a FITS Spectrum compatible with IRAF.  
You simply provide an extension type and a folder name (absolute or relative) and the code will automatically look for all files with that extension inside the folder.  
The FITS files will be created at the same hierarchy that the original file.

## Running

First, add execute privileges to the `.py` file. In linux, this can be achieved with `chmod +x ascii2fits.py`.  

To run the code, provide two arguments:

- Name of the folder for the program search for ascii files;
- Name of the extension to search for.

Example: `./ascii2fits.py folder_name .txt`

## File Structure

1. The first column must be wavelength values;
2. and the second one, flux values.


**By default, the code skips the first two lines of the file, be aware of that!**