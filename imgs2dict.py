import glob

import cv2
import numpy as np

from PIL import Image

from util import write_json_file
from config import FRAMES_JPG_PATH, DICT_PATH

def main():
    d = {}
    for path in glob.glob(FRAMES_JPG_PATH):
        # The avg_color is an numpy.ndarray with 3 numpy.float64 values
        # This is an RGB color
        avg_color = calc_avg_color(path)

        # The data type of the numbers in the ndarray is `numpy.float64`
        #print(f'{path}\t{avg_color}\t{type(avg_color)}\t{type(avg_color[0])}')

        path = path.replace("\\", "/")
        d[path] = avg_color.tolist()
    
    print(write_json_file(DICT_PATH, d))

def calc_avg_color(img_path: str):
    img = Image.open(img_path)
    np_img = np.array(img)
    avg_color: np.ndarray = np_img.mean(axis=(0, 1))
    img.close()
    return avg_color

if (__name__ == "__main__"):
    main()