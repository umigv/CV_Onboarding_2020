#!/usr/bin/env python3
# write your URL display code here!

# run these two commands to launch your URL display program:
# source devel/setup.bash
# rosrun url_display oled_display.py

# run these two commands to launch random url publisher:
# source devel/setup.bash
# rosrun qr_scan random_url.py

import rospy
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO

from std_msgs.msg import String

display = Adafruit_SSD1306.SSD1306_128_64(rst=None)
# Setups
display.begin()  # initialize graphics library for selected display module
display.clear()  # clear display buffer
display.display()  # write display buffer to physical display
displayWidth = display.width  # get width of display
displayHeight = display.height  # get height of display
image = Image.new('1', (displayWidth, displayHeight))  # create graphics library image buffer
draw = ImageDraw.Draw(image)  # create drawing object
font = ImageFont.load_default()  # load and set default font
# Draw text
draw.text((0,0), "Hello,\nRaspberry Pi!", font=font, fill=255)  # print text to image buffer
# Display to screen
display.image(image)  # set display buffer with image buffer
display.display()  # write display buffer to physical display
# Cleanup
GPIO.cleanup()  # release all GPIO resources

def callback(data):
    message = "Recieved URL: " + data
       
def listener(): 
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("url1", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
if __name__ == '__main__':
    listener()