import cv2
import numpy as np
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),'..','helper'))
import utilities
import Request
from Request import Request

image = cv2.imread("/home/vijayaganesh/Downloads/IMG_1583.jpg")
img_array = cv2.imencode('.jpg', image)[1].tostring()
request = Request(img_array)
print(request.response)
