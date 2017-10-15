import tensorflow as tf
import numpy as np
import os,glob,cv2
import sys,argparse
from google.cloud import vision
from google.cloud.vision import types

def predict_tf_logo(image):
    image_size=300
    num_channels=3
    images = []
    image = cv2.resize(image, (image_size, image_size), cv2.INTER_LINEAR)
    cv2.imshow('output',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    images.append(image)
    images = np.array(images, dtype=np.uint8)
    images = images.astype('float32')
    images = np.multiply(images, 1.0/255.0)
    cv2.imshow('output',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    x_batch = images.reshape(1, image_size,image_size,num_channels)
    sess = tf.Session()
    saver = tf.train.import_meta_graph(Constant.Classifier_Model)
    saver.restore(sess, tf.train.latest_checkpoint(Constant.Classifier_location))
    graph = tf.get_default_graph()
    y_pred = graph.get_tensor_by_name("y_pred:0")
    x= graph.get_tensor_by_name("x:0")
    y_true = graph.get_tensor_by_name("y_true:0")
    y_test_images = np.zeros((1, 3))
    feed_dict_testing = {x: x_batch, y_true: y_test_images}
    result=sess.run(y_pred, feed_dict=feed_dict_testing)
    result_dict = zip(Constant.classes,result)
    return sorted(result_dict, key = result_dict.get, reverse = True)[0]

def predict_vision_logo(image):
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=image)
    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    if len(logos) == 0:
        return None
    else
        for logo in logos:
            return logo.description

def predict_vision_label(image):
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=image)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    if len(labels) == 0:
        return None
    else
        for label in labels:
            return logo.description
