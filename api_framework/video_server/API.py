import hug
from PIL import Image, ImageDraw

@hug.get(output=hug.output_format.mp4_video, versions=1)
def watch():
    """Watch an example movie, streamed directly to you from pinkhelium"""
    return 'movie.mp4'

@hug.get('/watch2',output=hug.output_format.mp4_video, versions=2)
def watch():
    """Watch an example movie, streamed directly to you from pinkhelium"""
    return 'movie.mp4'

@hug.get('/image.png', output=hug.output_format.png_image)
def create_image():
    image = Image.new('RGB', (100, 50)) # create the image
    ImageDraw.Draw(image).text((10, 10), 'pinkhelium', fill=(255, 0, 0))
    return image