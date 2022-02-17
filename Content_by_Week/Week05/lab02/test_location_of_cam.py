import cv2
import time

# this is accessing my Ubuntu/Linxux /dev/ folder to check
# probably you have different path
# I can check the available options by running `ls /dev/video*` at CLI
# mine shows video0, video1, video5, video6 right now
cap = cv2.VideoCapture('/dev/video5')
# allow the camera to warmup
time.sleep(0.1)
ret, frame = cap.read()
print(ret, frame)