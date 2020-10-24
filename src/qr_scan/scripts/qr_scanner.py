#!/usr/bin/env python3
# Write your QR scanner code here!

# run these two commands to launch your qr scanner code:
# source devel/setup.bash
# rosrun qr_scan qr_scanner.py

# run these two commands to launch fake display program:
# source devel/setup.bash
# rosrun url_display fake_display.py

import cv2
import time
from picamera.array import PiRBGArray
from picamera import PiCamera


# initialize camera and grab reference to raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow camera to sleep for 0.1 sec
time.sleep(0.1)

# get image from camera
camera.Capture(rawCapture, format ="bgr")
image = rawCapture.array

#display image on screen and wait for key press
cv2.imshow("Image", image)
cv2.waitKey(0)


# CONVERTING QR CODE TO STRING

if len(sys.argv) > 1:
	inputImage = cv2.imread(sys.argv[1])
else:
	inputImage = cv2.imread("qr_codes/screen-0.jpg")
  
  
decodedObjects = pyzbar.decode(inputImage)

print(decodedObjects[0].data)


