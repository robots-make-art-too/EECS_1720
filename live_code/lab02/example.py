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

# We need to set resolution -> convert them from float to integer
frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)


# did we detect a video?
# save if we did
result = cv2.VideoWriter('vid/output.avi',
                         cv2.VideoWriter_fourcc('M','J','P','G'),
                         10, size)

while(video.isOpened()):

  # try to read if video is available
  # res, image = cam.read()
  ret, frame = video.read()

  # short confirmation and loop to access camera, 

  if ret == True:

    # Write the frame into the
    # file 'output.avi' ^^ from before
    result.write(frame)

    # Display the frame
    # save it 
    cv2.imshow('Frame', frame)
    cv2.imwrite('img/Frame.png', frame)

    # grab by frame an image
    # save the image, (and the video)
    # add to an API function (we don't build these)

    statusMessage = "Hi I am an image!"
    api.update_status_with_media(statusMessage,"img/Frame.png")


    # Press q on keyboard
    # to stop the process and grab a photo!
    # (from the last frame or instance of the cv2.imwrite() & cv2.imShow())
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break

  # Break the loop condition
  else:
      break

# post (you could grab, read, etc)

# close# dont forget to release() 
# cam.release()
video.release()
result.release()

# Closes all the frames
cv2.destroyAllWindows()
# # or specifically
# cv2.destroyWindow('Frame')

print("The video was successfully saved")
