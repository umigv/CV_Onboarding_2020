#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

old_string = ''

def callback(data):
    global old_string
    print("Received URL: " + data.data + ' ' * (len(old_string) - len(data.data)), end='\r', flush=True)
    old_string = data.data

def listener():
    rospy.init_node("receiver", anonymous=True)
    rospy.Subscriber("url1", String, callback)
    print("Showing URLs on Display...")
    rospy.spin()

if __name__ == "__main__":
    listener()