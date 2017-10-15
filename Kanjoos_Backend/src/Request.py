#!/usr/bin/env python

"""Request.py: Incoming request to annotate the captured image are mapped to this class
    The images arrive as byte array and converted to desired format by protobuf or numpy.
    Implemented as part of the application for the HackGT Hackathon"""

__author__      = "Vijaya Ganesh Mohan"
__credits__     = ["Abhilash Arivanan","Gokkulasudan Rathnakumar"]
__email__       = "vmohan2@ncsu.edu"
__status__      = "Development"

import cv2
import numpy as np
import json

class Request(object):
    """ Request class has the following attributes:

        Attributes:
            img_bytearray: Byte array of the input image
            image: Converted image from the byte Array
            response: A json object with the annotated response
        Methods:
            generate_response() : Method to use annotating functions to generate the JSON response
    """


    def __init__(self,img_bytearray):
        self.img_bytearray = img_bytearray
        image = cv2.decode(np.fromstring(img_bytearray,np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        response = self.generate_response()

    def generate_response(self):
        logo_annotation_tf = utilities.predict_tf_logo(self.image)
        logo_annotation_vision = utilities.predict_vision_logo(self.img_bytearray)
        label_annotation_vision = utilities.predict_vision_label(self.img_bytearray)
        text_annotation_vision = utilities.predict_vision_text(self.img_bytearray)
        color_annotation_vision = utilities.predict_vision_color(self.img_bytearray)
        response = {}
        if (logo_annotation_vision == None):
            response['logo'] = logo_annotation_tf
        else
            response['logo'] = logo_annnotation_vision
        label_set = set()
        for labels in label_annotation_tf:
            label_set.add(labels)
        for labels in label_annotation_vision:
            label_set.add(labels)
        response['label'] = label_annotation_vision
        response['text'] = text_annotation_vision
        response['color'] = color_annotation_vision
        json_response = json.dump(response)
        print(json_response)
        return json_response
