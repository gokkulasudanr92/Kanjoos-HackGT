import cv2
import numpy as np
import sys
sys.path.append('/home/vijayaganesh/Python_Workspace/Kanjoos/src/helper')
import utilities

INPUT_IMAGE_HEIGHT = 250
INPUT_IMAGE_WIDTH = 250
CONVOLUTION_FILTER_1_WIDTH = 5
CONVOLUTION_FILTER_1_HEIGHT = 5

classes = ['nike','adidas','reebok','cocacola','pepsi','Google','Sony','Dell','xbox','ps4']
num_of_classes = len(classes)
