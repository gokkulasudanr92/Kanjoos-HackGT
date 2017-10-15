from django.db import models

# Create your models here.
class Course(models.Model):
	title = models.CharField(max_length=255)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.title

class Review(models.Model):
	course = models.ForeignKey(Course, related_name='reviews')
	name = models.CharField(max_length=255);
	email = models.EmailField()
	comment = models.TextField(blank=True, default='')
	rating = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ['email', 'course']

	def __str__(self):
		return '{0.rating} by {0.email} for {0.course}'.format(self)

class ImageInfo(models.Model):
	imageUri = models.TextField(blank=False,null=False)
	color = models.TextField(blank=True,null=True)
	logo = models.TextField(blank=True,null=True)
	text = models.TextField(blank=True,null=True)
	label = models.TextField(blank=True,null=True)
	status = models.IntegerField(default=0)

	def __str__(self):
		return self.imageUri

class ImageURI(models.Model):
	image = models.ForeignKey(ImageInfo, related_name='image')
	uri = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.uri