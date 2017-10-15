from google.cloud import vision
from google.cloud.vision import types
import io
import os
import cv2

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = '/home/vijayaganesh/Downloads/Sony/61SaT9ZFP1L.jpg'

image = cv2.imread(file_name)
image_bytearray = cv2.imencode('.jpg',image)[1].tostring()
# Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()
# # print(content)
# print(type(image_file))
image = types.Image(content=image_bytearray)

# Performs label detection on the image file
# response = client.text_detection(image=image)
# labels = response.text_annotations
# print(labels)

# print('label:')
# for label in labels:
#     print(label.description)

response = client.image_properties(image=image)
props = response.image_properties_annotation
print('Properties:')
for color in props.dominant_colors.colors:
    print('fraction: {}'.format(color.pixel_fraction))
    print('\tr: {}'.format(color.color.red))
    print('\tg: {}'.format(color.color.green))
    print('\tb: {}'.format(color.color.blue))
    print('\ta: {}'.format(color.color.alpha))
