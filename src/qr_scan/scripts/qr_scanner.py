#!/usr/bin/env python3
# Write your QR scanner code here!

# run these two commands to launch your qr scanner code:
# source devel/setup.bash
# rosrun qr_scan qr_scanner.py

# run these two commands to launch fake display program:
# source devel/setup.bash
# rosrun url_display fake_display.py

import cv2
import numpy as np
import sys
import requests
import time
from pathlib import Path

print("hello world this is the qr scanner")

# print(Path('.').absolute())
# r = requests.get("https://live.staticflickr.com/3048/2854521482_5bd41a2e1b_b.jpg").content
# #r = requests.get(sys.argv[1]).content
# nparr = np.frombuffer(r, np.uint8)
# inputImage = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
# # inputImage = cv2.imread(sys.argv[1])

# def display(im, bbox):
#     n = len(bbox)
#     for j in range(n):
#         cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255, 0, 0), 3)
#     cv2.imshow("Results", im)

# qrDecoder = cv2.QRCodeDetector()

# data, bbox, rectifiedImage = qrDecoder.detectAndDecode(inputImage)
# if len(data)>0:
#     print("Decoded Data : {}".format(data))
#     display(inputImage, bbox)
#     rectifiedImage = np.uint8(rectifiedImage)
#     cv2.imshow("Rectified QRCode", rectifiedImage)
# else:
#     print("QR Code not detected")
#     cv2.imshow("Results", inputImage)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
