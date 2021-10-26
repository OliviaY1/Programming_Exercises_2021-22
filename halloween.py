# Image Magic
# Load on image and manipulate the pixels

from PIL import Image

# Load the image (pumpkin)
image = Image.open('venv/halloween-unsplash.jpg')  # double quotes are used in string, single quote is a symble
output_image = Image.open('venv/halloween-unsplash.jpg')
# Modify the image to convert it from colour to gray
# (rgb) -> ()
# Iterate over EVERY PIXEL
width = image.width
height = image.height
# Top bottom
def to_greyscale(pixel):
    '''Convert a pixel to greyscale
    Arug:
        pixel: a 3-tuple of ints from
            0 - 255, e.g.(140,120,255)
            represents(red, green, blue)
    Returns:
        a 3-tuple pixel (r, g, b) in
        greyscale

    '''
    a= sum(pixel) // 3
    return a+10,a+10,a+10

def to_greyscale_luma(pixel: tuple) -> tuple:
    r,g,b = pixel
    a= int(r*0.3+g*0.59+b*0.11)
    return a,a,a

def to_greyscale_red(pixel: tuple) ->tuple:
    r,g,b = pixel
    return r,r,r
def to_greyscale_blue(pixel: tuple) ->tuple:
    r,g,b = pixel
    return b,b,b

def decide_func(pixel: tuple, algo="average") -> tuple:
    ''' convert a pixel to greyscale.
    can also specify the greyscale algorithm.
    defaults to average

    Argus:
        pixel: a 3-tup;le of ints
        algo: the greyscale conversion algorithm
            specified by the star
            valid values are "avergage", "luma"
    '''
    if algo == 'luma':
        return to_greyscale_luma(pixel)
    elif algo == 'red':
        return to_greyscale_red(pixel)
    elif algo == 'blue':
        return to_greyscale_blue(pixel)
    elif algo == 'brightness':
        return brightness(pixel)
    else:
        return to_greyscale(pixel)

def brightness(pixel: tuple, magnitude: int) -> tuple:
    red,green,blue = pixel
    MAX = 255
    MIN = 0

    # add the magnitude to the r,g,b values
    if red+magnitude > MAX:
        red = MAX
    elif red+magnitude < MIN:
        red = MIN
    else:
        red += magnitude

    if green+magnitude > MAX:
        green = MAX
    elif green+magnitude < MIN:
        green = MIN
    else:
        green += magnitude

    if blue+magnitude > MAX:
        blue = MAX
    elif blue+magnitude < MIN:
        blue = MIN
    else:
        blue += magnitude
    return red, green, blue

for y in range(height):
    for x in range(width):
        p = image.getpixel((x, y))
        # TODO:
        a = brightness(p, -100)
        output_image.putpixel((x,y), a)
        # create a new pixel
        # TODO: put that in the new image
output_image.save('brighten.jpg')
