#!/usr/bin/env python3
# write your URL display code here!

# run these two commands to launch your URL display program:
# source devel/setup.bash
# rosrun url_display oled_display.py

# run these two commands to launch random url publisher:
# source devel/setup.bash
# rosrun qr_scan random_url.py

import rospy
from std_msgs.msg import String

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class Display:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        i2c = busio.I2C(SCL, SDA)
        self.disp = adafruit_ssd1306.SSD1306_I2C(width, height, i2c)
        self.disp.fill(0)
        self.disp.show()
        self.image = Image.new("1", (width, height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf')

    def clear(self):
        self.disp.fill(0)
        self.disp.show()

    def show_text(self, text):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.draw.text((0, 0), text, font=self.font, fill=255)
        self.disp.image(self.image)
        self.disp.show()

def callback(data, disp):
    print("Received URL:", data.data)
    disp.show_text(data.data)

def listener():
    rospy.init_node("receiver", anonymous=True)
    oled_display = Display(128, 64)
    rospy.Subscriber("url", String, callback, oled_display)
    print("Showing URLs on Display...")
    rospy.spin()
    oled_display.clear()

if __name__ == "__main__":
    listener()