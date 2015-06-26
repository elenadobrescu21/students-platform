from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)
	forum = models.ForeignKey('Forum') # referinta la Forum
	upload = models.FileField("Upload a file", upload_to = 'media', null=True, blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title

class Forum(models.Model):
	title = models.CharField(max_length=200)
	published_date = models.DateTimeField(
			blank=True, null=True)
	def __str__(self):
		return self.title
