# libraries

import cv2 # specific for accessing the camera and handling this type of live media

import time # so we can pause for the camera to warm up or initate 
import sys # this is system - in case we want to access system
import imutils # think of my as a utility library
from PIL import Image # image handling library
import os # to access the OS so saving files or direct command line etc


import tweepy #  twitter API 

#####
#
# YOU MAY NEED TO INSTALL THE LIBRARIES 
#
#####


# authentification

# require some sort of account access - so make a new one or a dummy something
# there will be some developer or token activation or generation
#

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# we need to identify and define the way we will use the API
# how we call the API
api = tweepy.API(auth)

# load my authetifciation keys/tokens from a file

# my choice of media is video/images direct from my camera/webcam

# video camera capture
cam_port = 2 #0,1
video = cv2.VideoCapture("filename.ext") 
# this integer could also be a file name 
# or the integer indicates a camera attached and if more than one which one

# We need to check if camera isOpened()
if (video.isOpened() == False):
  print("Error reading video file")



# short confirmation and loop to access camera, 
# grab by frame an image
# save the image, (and the video)
# add to an API function (we don't build these)

    statusMessage = "Hi I am an image!"
    api.update_status_with_media(statusMessage,"img/Frame.png")

# post (you could grab, read, etc)

# close

