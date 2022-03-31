# libraries

# don't forget those other python codes from lecture last week - image rotation, resize ... etc
# could be useful ?

import cv2 # specific for accessing the camera and handling this type of live media

import time # so we can pause for the camera to warm up or initiate 
import sys # this is system - in case we want to access system
import imutils # think of me as a utility library - for im or images
from PIL import Image # image handling library _ PIL is for Pillow
# so can also pip install (then import) Pillow
import os # to access the OS so saving files or direct command line etc


import tweepy #  twitter API 

#####
#
# YOU MAY NEED TO INSTALL THE LIBRARIES 
#
#####

# authentification process
# will require some sort of account access - so make a new one or a dummy something
# there will be some developer or token activation or generation
# your LAB02 part a) exercise is to explicitly document the process in obtaining and applying the access/tokens/keys/steps
# for 3 different social media platforms (anything: blogs, website builders, reddit, insta, twitch, etc etc etc)
#
tokens = [] # I'm a python list, I can be `.append()` -ed 

# we could store those keys in a separate file -- in fact please do and then don't upload the file to your repo
# just upload the code that uses the file
# load my authentication keys/tokens from a file
# this then assumes that I've placed my twitter tokens - of which I need 4 - into a file.txt where each line is one of the tokens
with open('file.txt', 'r') as f:
  for line in f:
    tokens.append(line.strip()) 

consumer_key = tokens[0] # I could assign my tokens to variables like this
consumer_secret = '' # if we wanted to add the tokens/keys directly as strings instead of reading a file
access_token = ''
access_token_secret = ''

# twitter/tweepy specific auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# we need to identify and define the way we will use the API
# how we call the API
api = tweepy.API(auth)

# my choice of media is video/images direct from my camera/webcam
# video camera capture
cam_port = 2 # 0,1.. - depends on if/how many cameras attached
# but not necessarily literally - for me 5 is associated with where the camera access is stored

# VideoCapture(cam_port) can work too 
video = cv2.VideoCapture(5) 
# I could also instead load a video file by replacing the integer `5` here with "filename.ext" e.g., "mymovie.avi"
# so this integer `5` could be a file name or it could indicates a camera and if more than one camera - which one

# We need to check if camera isOpened()
# it's like checking if our mouse is Pressed (def mousePressed(): from our processing.py examples)
if (video.isOpened() == False):
  print("Error reading video file")

# We need to set resolution -> convert them from float to integer
frame_width = int(video.get(3))
frame_height = int(video.get(4))
# just making one object/variable to handle the combined height and width, as they usually go together
size = (frame_width, frame_height)

# did we detect a video?
# save if we did
# leave the cv2.VideoWriter_fourcc parts alone unless you know why you might change it
result = cv2.VideoWriter('vid/output.avi',
                         cv2.VideoWriter_fourcc('M','J','P','G'),
                         10, size)

while(video.isOpened()):
  # try to read if video is available
  res, frame = video.read()

  # short confirmation and loop to access camera, 
  # we will grab an image by frame
  # and save the image, (and the video)
  if res == True:
    # Write the frame into the
    # file 'output.avi' ^^ from before
    result.write(frame)

    # Display the frame
    # save it 
    cv2.imshow('Frame', frame)
    cv2.imwrite('img/Frame.png', frame)

    # Press q on keyboard - or something else, try it
    # to stop the process and grab a photo!
    # (from the last frame or instance of the cv2.imwrite() & cv2.imShow())
    if cv2.waitKey(1) & 0xFF == ord("q"):

      #####
      # let us only post one image to twitter, the last access instead of the continuous frame grabs
      ####
      
      # add to an API function (we don't build these)
      # post (you could grab, read, etc)
      statusMessage = "Hi I am an image!"
      api.update_status_with_media(statusMessage,"img/Frame.png") 
      
      # this is where you will get creative what and how and why will you access 
      # there are many ways to interact with, access, or generated, content
     
      break

  # Break the loop condition
  # we don't want to loop forever; also format
  else:
      break

# close
# dont forget to release() 
video.release()
result.release()

# closes all the frames
cv2.destroyAllWindows()
# or specifically if it is useful cv2.destroyWindow('Frame') where Frame was the name from cv2.imshow('Frame', frame)

# because why not
print("yay")
text = 'yay'
print(".. ", text) # another way
