# vid2pixels.py

Turn video frames into pixels for an image

- [How to use](#how-to-use)
- [Example](#example)
- [How does it work?](#how-does-it-work)

## How to use

1. Install requirements in [requirements.txt](./requirements.txt)

2. Set up the paths in [config.py](./config.py) and [convert.py](./convert.py)

3. Run [vid2imgs.py](./vid2imgs.py)

4. Run [imgs2dict.py](./imgs2dict.py)

5. Run [convert.py](./convert.py)

## Example

Input video: [Rick Astley - Never Gonna Give You Up (Official Music Video)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

Input image:

<img src="./examples/input-image.jpg" alt="input" width="200">

Output image:

<img src="./examples/output-lenna-158.jpg" alt="output" width="200">

Zoom in of the output image:

<img src="./examples/zoom-in.png" alt="output-zoom-in">

## How does it work?

1. Extract frame from the video every N millisecond, then crop it's center out as a square image, resize it and save it. (Set it to 1000 to extract a frame every 1 second)

2. Loop through every images saved, calculate the average color of them and save the calculation result as a JSON file.

3. Loop through every pixels in the input image, find the closest image of that pixel's color. Then paste the closest image to the output image file.
