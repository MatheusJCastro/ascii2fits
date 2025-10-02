from astropy.io import fits
import astropy.units as u
import pandas as pd
import numpy as np


def open_spec(fl_name):
    # Subroutine to open the .fits spectrum and read it

    hdul = fits.open(fl_name)  # open the file
    spec_data = hdul[0].data  # get the data
    spec_header = hdul[0].header  # get the header

    # Convert units, if needed
    # if len(np.shape(spec_data)) == 2:
    #     spec_data = spec_data[1] * 10**-17 * u.Unit('erg cm-2 s-1 AA-1')
    # else:
    #     spec_data = spec_data * 10**-17 * u.Unit('erg cm-2 s-1 AA-1')

    # Get the wavelength information from the header
    # CDELT1 or CD1_1
    wl = spec_header['CRVAL1'] + spec_header['CDELT1'] * np.arange(0, len(spec_data))
    wl = wl * u.AA  # * 10

    hdul.close()  # close the file

    return pd.DataFrame(data={"wl": wl, "data": spec_data})


fl = "bulge6-bri_u3svrg2.fits"
spec = open_spec(fl)

spec.to_csv(fl[:-4] + ".csv", sep=",", header=False, index=False)