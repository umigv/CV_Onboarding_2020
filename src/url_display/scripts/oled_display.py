#!/usr/bin/env python3
# write your URL display code here!

# run these two commands to launch your display code:
# source devel/setup.bash
# rosrun url_display oled_display.py

# run these two commands to launch fake qr scanner program:
# source devel/setup.bash
# rosrun qr_scan random_url.py

import rospy
from std_msgs.msg import String

import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("url", String, callback)
    rospy.spin()
  

if __name__ == '__main__':
	listener()
  
  
# 2nd site part
# puts writing on OLED display


 
# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
 
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
 
# Clear display.
disp.fill(0)
disp.show()
 
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
 
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
 
 
# Load default font.
font = ImageFont.load_default()
 
# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)
 
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
 
    # Shell scripts for system monitoring from here:
   
 
    # Write four lines of text.
 
    draw.text((x, top + 0), "IP: " + IP, font=font, fill=255)
 
    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(0.1)
  
