import os

import cv2
import numpy as np

from typing import Union

from util import mkdirs
from config import VIDEO_PATH, FRAMES_PATH

def main():
    RESIZE_SIZE = 32
    SCALE_FACTOR = 0.1
    SKIP_MS = 250

    mkdirs(FRAMES_PATH)

    # From: https://stackoverflow.com/a/47632941
    # Feels like this loop logic isnt right?...
    count = 0
    vidcap = cv2.VideoCapture(VIDEO_PATH)
    success, img = vidcap.read()
    while (success):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, count * SKIP_MS)
        success, img = vidcap.read()
        if (img is None):
            continue

        cropped = crop(img)
        resized = resize(cropped, RESIZE_SIZE)
        cv2.imwrite(f'{FRAMES_PATH}/frame-{count}.jpg', resized)
        count += 1
    
    vidcap.release()
    print("--- End of Program ---")

def resize(img: np.ndarray, new_size: int=None, scale_factor: Union[int, float]=None) -> np.ndarray:
    """Resizes an image with either dsize or scale factor, one of them has to be provided

    Args:
        img (np.ndarray): Image to be resized
        new_size (int, optional): New size for both height and width. Defaults to None.
        scale_factor (Union[int, float], optional): Scale factor, `int` or `float`. Defaults to None.

    Raises:
        Exception: Raised when both `new_size` and `scale_factor` are None

    Returns:
        np.ndarray: Resized image
    """
    if (new_size != None):
        return cv2.resize(img, (new_size, new_size))

    if (scale_factor != None):
        return cv2.resize(img, None, fx=SCALE_FACTOR, fy=SCALE_FACTOR)

    raise Exception("Both `new_size` and `scale_factor` cannot be None at the same time")

def crop(img: np.ndarray):
    """Crops an image to square from it's center

    Args:
        img (np.ndarray): Input image

    Returns:
        np.ndarray: Cropped image
    """
    h, w = img.shape[0], img.shape[1]
    size = min(h, w)
    cx, cy = w // 2, h // 2

    x_start = cx - size // 2
    y_start = cy - size // 2
    x_end = x_start + size
    y_end = y_start + size

    cropped = img[y_start:y_end, x_start:x_end]
    return cropped

if (__name__ == "__main__"):
    main()