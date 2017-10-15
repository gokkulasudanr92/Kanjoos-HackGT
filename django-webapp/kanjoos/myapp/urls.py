from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.ListCreateCourse.as_view(), name='course_list'),
	url(r'data$', views.ListCreateImageInfo.as_view(), name='image_list'),
	url(r'data/(?P<pk>[0-9]+)/$', views.ImageInfoDetail.as_view(), name='image_detail'),
]