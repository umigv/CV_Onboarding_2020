#!/usr/bin/env python3
# Write your QR scanner code here!

# run these two commands to launch your qr scanner code:
# source devel/setup.bash
# rosrun qr_scan qr_scanner.py

# run these two commands to launch fake display program:
# source devel/setup.bash
# rosrun url_display fake_display.py
from __future__ import print_function
from picamera.array import PiRGBArray
from picamera import PiCamera
import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np
import sys
import time
import rospy
from std_msgs.msg import String

# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)

def QRScanner_opencv(image):
    qrDecoder = cv2.QRCodeDetector()
    # Detect and decode the qrcode
    ros,bbox,rectifiedImage = qrDecoder.detectAndDecode(img)
    if len(data)>0:
        print("Decoded Data : {}".format(data))
        rectifiedImage = np.uint8(rectifiedImage)
        return data
    else:
        return "QR Code not detected"

def QRScanner_zbar(image):
    decodedObject = pyzbar.decode(image)
    if len(decodedObject) == 0:
        print("No QR Code Detected")
        return "No QR Code Detected"
    else:
        print("Decoded Data: " + decodedObject[0].data.decode())
        return decodedObject[0].data.decode()


def talker():
    # Initialize the camera
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
    # Let the camera warm up
    time.sleep(0.1)
    # Declares string "pub" to be published to the url1 topic
    pub = rospy.Publisher('url1', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array
        rawCapture.truncate()
        rawCapture.seek(0)
        # Collects the string for the URL using the zbar function
        data = QRScanner_zbar(image)
        cv2.imshow("title", image)
        theURL = data
        # Publishes the URL string to ROS
        pub.publish(theURL)
        rate.sleep() 

# Calls talker() when program is run
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
