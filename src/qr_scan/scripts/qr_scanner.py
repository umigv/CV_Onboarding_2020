# run these two commands to launch your qr scanner code:
# source devel/setup.bash
# rosrun qr_scan qr_scanner.py

# run these two commands to launch fake display program:
# source devel/setup.bash
# rosrun url_display fake_display.py

import cv2
import time
import numpy as np
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera
import rospy
from std_msgs.msg import String


# initialize camera and grab reference to raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow camera to sleep for 0.1 sec
time.sleep(0.1)




# WRITING THE PUBLISHER NODE

def talker():
	pub = rospy.Publisher('url', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
  	# get image from camera
		camera.Capture(rawCapture, format ="bgr")
		image = rawCapture.array

		#display image on screen and wait for key press
		#cv2.imshow("Image", image)
		#cv2.waitKey(0)

		#if len(sys.argv) > 1:
		#	inputImage = cv2.imread(sys.argv[1])
		#else:
		#	inputImage = cv2.imread("qr_codes/screen-0.jpg")
      
		decodedObjects = pyzbar.decode(image)
		print(decodedObjects[0].data)
    hello_str = decodedObjects.data
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    



if __name__ == '__main__':
  try:
  	talker()
  except rospy.ROSInterruptException:
  	pass



