import cv2
import numpy as np
image = cv2.imread('/home/vijayaganesh/Downloads/IMG_1566.jpg')
color = ('b','g','r')
hist = np.zeros((256,3))
print(hist.shape)
# print(hist)

for i,col in enumerate(color):
    print(cv2.calcHist([image],[i],None,[256],[0,256]))
    hist[:i] = cv2.calcHist([image],[i],None,[256],[0,256])
print(hist.shape)
