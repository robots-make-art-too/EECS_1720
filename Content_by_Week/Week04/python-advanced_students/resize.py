from PIL import Image
import argparse
import sys
 
parser = argparse.ArgumentParser(description="Resize an image")
 
parser.add_argument("image", nargs="?", help="Image", default=None)
parser.add_argument("width", nargs="?", type=int, help="Width", default=None)
parser.add_argument("height", nargs="?", type=int, help="Height", default=None)
 
arguments = parser.parse_args()
 
use_arguments_image = True if arguments.image is not None else False
use_arguments_width = True if arguments.width is not None else False
use_arguments_height = True if arguments.height is not None else False
 
# Validation for image file name
while True:
    if use_arguments_image:
        image = arguments.image
    else:
        image = input("Enter the image file name: ")
 
    try:
        im = Image.open(image)
    except:
        print("Invalid image")
        if use_arguments_image:
            sys.exit()
        continue
    break
 
# Validation for width
if use_arguments_width:
    width = arguments.width
else:
    while True:
        print("Current resolution is (w, h): " + str(im.size))
        width = input("Enter the new width: ")
        try:
            width = int(width)
        except:
            print("Invalid width")
            continue
        break
 
# Validation for height
if use_arguments_height:
    height = arguments.height
else:
    while True:
        print("Current resolution is (w, h): " + str(im.size))
        height = input("Enter the new height: ")
        try:
            height = int(height)
        except:
            print("Invalid height")
            continue
        break
 
im_resize = im.resize((width, height), resample=Image.BICUBIC)
im_resize.save("resized_" + image)