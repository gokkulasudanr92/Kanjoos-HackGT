from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

import io,sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),'src','helper'))
print(os.path.join(os.path.dirname(__file__),'src','helper'))
import utilities
sys.path.append(os.path.join(os.path.dirname(__file__),'src','runner'))
from Request import Request
sys.path.append(os.path.join(os.path.dirname(__file__),'src','constants'))
import Constant
import cv2
import numpy as np
import base64

# Add Imports here

def index(req):
	return render(req, 'index.html', {'STATIC_URL': settings.STATIC_URL})

class ListCreateCourse(APIView):
	def get(self, request, format=None):
		courses = models.Course.objects.all()
		serializer = serializers.CourseSerializer(courses, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = serializers.CourseSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

def list(req):
	# Logic to get list of the data
	# Integrate the JSON here
	images = models.ImageInfo.objects.all()
	print(type(images))
	for image in images:
	    # print(type(image.imageUri))
	    image_string = base64.b64decode(image.imageUri[23:])
	    # print(image_string)
	    request = Request(image_string)
	    image.logo = request.response['logo']
	    image.label = request.response['label']
	    image.text = request.response['text']
	    image.color = request.response['color']

	    image.save()
		# For image format refer in models.py file in myapp folder
	list = models.ImageInfo.objects.all()
	'''result = []
	for item in list:
	    temp = {};
	    temp["id"] = item.id
	    temp["logo"] = item.logo
	    temp["text"] = item.text
	    temp["color"] = item.color
	    result.append(temp);'''

	context={
	  'result': list,
	  'STATIC_URL': settings.STATIC_URL
	}
	return render(req, 'list.html', context)

class ListCreateImageInfo(APIView):
	@csrf_exempt
	def get(self, request, format=None):
		images = models.ImageInfo.objects.all()
		serializer = serializers.ImageSerializer(images,many=True)
		return Response(serializer.data)

	@csrf_exempt
	def post(self, request, format=None):
	    serializer = serializers.ImageSerializer(data=request.data)
	    serializer.is_valid(raise_exception=True)
	    serializer.save()
	    return Response(serializer.data, status=status.HTTP_201_CREATED)

class ImageInfoDetail(APIView):
	@csrf_exempt
	def get_object(self, pk):
		try:
			return models.ImageInfo.objects.get(pk=pk)
		except models.ImageInfo.DoesNotExist:
			raise Http404

	@csrf_exempt
	def get(self, request, pk, format=None):
		image = self.get_object(pk)
		serializer = serializers.ImageSerializer(image)
		return Response(serializer.data)

	@csrf_exempt
	def put(self, request, pk, format=None):
		image = self.get_object(pk)
		serializer = serializers.ImageSerializer(image, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
