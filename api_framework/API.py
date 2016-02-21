import hug
from PIL import Image, ImageDraw

@hug.get(output=hug.output_format.mp4_video, versions=1)
def watch():
    """Watch an example movie, streamed directly to you from pinkhelium demonstrating the power of our api platform"""
    return 'movie.mp4'

@hug.get('/watch2',output=hug.output_format.mp4_video, versions=2)
def watch():
    """Watch an example movie, streamed directly to you from pinkhelium. This is version 2 of the popular watch api."""
    return 'movie.mp4'

@hug.get('/image', output=hug.output_format.png_image)
def create_image(text):
    image = Image.new('RGB', (500, 500))
    ImageDraw.Draw(image).text((100, 100), text, fill=(255, 0, 0))
    return image
	

@hug.get('/greet_user', versions=1)
def greet_user(values):
	'''Describe Your Function Here!'''
	return("Welcome to pinkhelium" + values)

	

@hug.get('/dummy', versions=4)
def dummy(values):
	'''Describe Your Function Here!'''
	return(values)
	

@hug.get('/deploy', versions=3)
def deploy(values):
	'''deploy function is this!'''
	return("DEPLOYED")
	

@hug.get('/deploy2', versions=4)


def deploy2(values):
	'''Describe Your Function Here!'''
	return("Hello World")
	

