import sys
# import skvideo.io
import numpy as np
import cv2

# cap = skvideo.io.VideoCapture('video_sample.avi')
# ret, frame = cap.read()


    
cap = cv2.VideoCapture('http://172.22.22.221/mjpg/video.mjpg')
# cap = cv2.VideoCapture(0)

if not cap.isOpened():
	print("does not work")
	exit()
    
fgbg = cv2.createBackgroundSubtractorKNN()

while(1):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	fgmask = fgbg.apply(blurred)
	cv2.imshow('frame',fgmask)
	cv2.imshow('video',frame)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
