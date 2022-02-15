# Tuesday February 15 | Week 06

import cv2 # specific for accessing the camera and handling this type of live media

import time # so we can pause for the camera to warm up or initiate 
import sys # this is system - in case we want to access system
import imutils # think of me as a utility library - for im or images
from PIL import Image # image handling library _ PIL is for Pillow
# so can also pip install (then import) Pillow
import os # to access the OS so saving files or direct command line etc



cam_port = 2 # 0,1.. - depends on if/how many cameras attached


video = cv2.VideoCapture(5) 

if (video.isOpened() == False):
  print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

result = cv2.VideoWriter('vid/output.avi',
                         cv2.VideoWriter_fourcc('M','J','P','G'),
                         10, size)

while(video.isOpened()):
  
  res, frame = video.read()

  if res == True:
    result.write(frame)

    cv2.imshow('Frame', frame)
    cv2.imwrite('img/Frame.png', frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):

      statusMessage = "Hi I am an image!"
     
      break

  else:
      break

video.release()
result.release()

cv2.destroyAllWindows()

print("yay")
text = 'yay'
print(".. ", text) # another way
