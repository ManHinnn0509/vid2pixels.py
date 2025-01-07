import numpy as np

from PIL import Image

from util import read_json_file
from config import DICT_PATH

def main():
    INPUT_IMG = './imgs/lenna-158.jpg'
    OUTPUT_PATH = "./output.jpg"

    d = read_img_dict(DICT_PATH)

    # Pre-load the frames that will be used as pixels
    preloaded = preload_img(d)

    # Read width, height from input image
    in_img = Image.open(INPUT_IMG)
    in_w, in_h = in_img.size

    # Prepare for output image
    size = min(Image.open(next(iter(d))).size)    
    out_img = Image.new('RGB', (in_w * size, in_h * size))

    # Load pixels from input image
    pixels = in_img.load()
    cw, ch = 0, 0
    for y in range(in_h):
        print(f"Current row: {y + 1} / {in_h}")
        for x in range(in_w):
            pixel = pixels[x, y]
            closest_img = find_closest_img(pixel, d)
            img = preloaded[closest_img]
            out_img.paste(img, (cw, ch))
            cw += size
        cw = 0
        ch += size

    # Close & save
    out_img.save(OUTPUT_PATH)
    in_img.close()

    print("--- End of Program ---")

def preload_img(d: dict):
    preloaded = {}
    for img_path in d.keys():
        img = Image.open(img_path)
        preloaded[img_path] = img
    
    return preloaded

def read_img_dict(path: str):
    """Reads the img dict, converts RGB value from `list` to `np.ndarray`

    Args:
        path (str): Path to the img dict

    Returns:
        d (dict): Converted dict from JSON file
    """
    d: dict = read_json_file(path)
    for k, v in d.items():
        v: list
        d[k] = np.asarray(v, dtype=np.float64)
    
    return d

def find_closest_img(color: tuple[int, int, int], d: dict) -> str:
    """Finds the closest image from given RGB value & dict

    Args:
        color (tuple[int, int, int]): Target color
        d (dict): Dict with image paths and average color values

    Returns:
        str: Closest image's path
    """
    closest_img_path = None
    closest_distance = float('inf')
    
    target_color = np.array(color)
    for img_path, avg_color in d.items():
        distance = np.linalg.norm(target_color - avg_color)
        if (distance < closest_distance):
            closest_distance = distance
            closest_img_path = img_path

    return closest_img_path


if (__name__ == "__main__"):
    main()