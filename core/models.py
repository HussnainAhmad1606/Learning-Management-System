from django.db import models

# Create your models here.
class Course(models.Model):
	course_id = models.AutoField(primary_key= True)
	course_name = models.CharField(max_length=70)
	course_description = models.CharField(max_length=200)
	course_photo = models.ImageField()
	course_link = models.CharField(max_length=200)

	def __str__(self):
		return self.course_name


class Video(models.Model):
	video_id = models.AutoField(primary_key=True)
	video_name = models.CharField(max_length=50)
	video_description = models.CharField(max_length=200)
	video_embed_code = models.CharField(max_length=300)
	video_category = models.ForeignKey(Course, default=0, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.video_name}"