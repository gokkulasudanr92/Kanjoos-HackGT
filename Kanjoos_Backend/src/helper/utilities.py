import tensorflow as tf
import numpy as np
import os,glob,cv2
import sys,argparse
from google.cloud import vision
from google.cloud.vision import types
import webcolors
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),'..','constants'))
import Constant
# print(Constant.Classifier_Model)
def predict_tf_logo(image):
    image_size=300
    num_channels=3
    images = []
    image = cv2.resize(image, (image_size, image_size), cv2.INTER_LINEAR)
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
    print('here')
    feed_dict_testing = {x: x_batch, y_true: y_test_images}
    result=sess.run(y_pred, feed_dict=feed_dict_testing).tolist()
    result_dict = dict(zip(Constant.classes,result))
    print(result_dict)
    return sorted(result_dict, key = result_dict.get, reverse = True)[0]

def predict_vision_logo(image):
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=image)
    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    if len(logos) == 0:
        return None
    else:
        for logo in logos:
            return logo.description

def predict_vision_label(image):
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=image)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    if len(labels) == 0:
        return None
    else:
        label_list = list()
        for i,label in enumerate(labels):
            label_list.append(label.description)
            if( i > 5):
                break
        return ','.join(label_list)

def predict_vision_text(image):
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=image)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if len(texts) == 0:
        return None
    else:
        text_list = list()
        for i,text in enumerate(texts):
            text_list.append(text.description)
            if( i > 5):
                break
        return ','.join(text_list)

def predict_vision_color(image):
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=image)
    response = client.text_detection(image=image)
    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    color_list = list()
    for i,color in enumerate(props.dominant_colors.colors):
        color_list.append(webcolors.rgb_to_hex((repr(color.color.red),repr(color.color.green),repr(color.color.blue))))
        if(i > 3):
            break
    return color_list
