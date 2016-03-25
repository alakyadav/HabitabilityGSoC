import os
from matplotlib import pyplot as plt
from fitsc import Fitsclass
from utils import *
import config

if __name__ == '__main__':
    file_path = os.getcwd() + "/files/"
    dirs = os.listdir(file_path)
    fits_obj_list = []

    gen = [i for i in dirs if i.endswith("fits")]
    for i in gen:
        fits_object = Fitsclass(file_path + i)
        fits_obj_list.append(fits_object)

    for obj in fits_obj_list:
        compare_and_add(obj)

    _, max_x, max_y = config.glob_max_dimen
    x_val = []
    y_val = []

    for obj in fits_obj_list:
        temp_x, temp_y = max_pix_vals(obj, max_x, max_y)
        x_val.extend(temp_x)
        y_val.extend(temp_y)

    plt.plot(x_val, y_val, 'k.')
    plt.xlabel('Time since J2000 epoch (seconds)')
    plt.ylabel('Flux')
    plt.title('Flux vs. Time lightcurve')
    plt.savefig('Flux vs. Time lightcurve.pdf')
    plt.close()
