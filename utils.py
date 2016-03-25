import config


def compare_and_add(obj):
    """
    Scan all the pixels of each image in the FITS image file row-wise,
    compare the flux value with that of the brightest pixel so far and
    if it is higher, set it as the new brightest pixel.

    Parameters
    ----------
    obj: Fitsclass
         Object of the class Fitsclass.
    """
    dimens, hdudata = obj.dimen, obj.hdudata
    for x in range(dimens[0]):
        for y in range(dimens[1]):
            for z in range(dimens[2]):
                pixel_val = hdudata[x][y][z]
                pixel_dim = (x, y, z)
                if pixel_val > config.glob_max_pixel:
                    config.glob_max_pixel = pixel_val
                    config.glob_max_dimen = pixel_dim


def max_pix_vals(obj, x, y):
    """
    Return a list of flux values for a particular pixel from each image
    in the FITS file along with the corresponding time.

    Parameters
    ----------
    obj: Fitsclass
    x: int
       Row number of the pixel
    y: int
       Column number of the pixel

    Returns
    -------
    temp_x: list
            List of values of time (secs) of capture.
    temp_y: list
            List of corresponding values of flux.
    """

    temp_x = []
    temp_y = []
    time = obj.time
    dimens, hdudata = obj.dimen, obj.hdudata
    for j in range(dimens[0]):
        val = hdudata[j][x][y]
        temp_y.append(val)
        temp_x.append(time)
        time += 2  # Each image captured after a 2 seconds interval.
    return temp_x, temp_y
