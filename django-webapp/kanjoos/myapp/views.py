from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

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