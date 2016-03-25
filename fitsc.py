from astropy.io import fits


class Fitsclass():
    """
    The class 'Fitsclass' is used to extract, store and retrieve relevant
    data and metadata from a FITS image file of Spitzer space telescope
    observations.
    """
    def __init__(self, i):
        """
        Open a FITS image file and save the data required to access
        image pixels.

        Parameters
        ----------
        i: str
           FITS file name along with the entire path.

        Attributes
        ----------
        hdudata: numpy.ndarray
                 Multidimensional array containing data cuboid.
        dimen: tuple
               Dimensions of data cuboid.
               dimen[1] images of dimen[2] rows and dimen[3] columns each.
        time: float
              DCE start time (TDB seconds past J2000).
        """

        hdulist = fits.open(i)
        self.hdudata = hdulist[0].data
        self.dimen = hdulist[0].shape
        self.time = hdulist[0].header['ET_OBS']
        hdulist.close()
