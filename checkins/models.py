from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Checkins(models.Model):
	#latitude,longitude,review,place name
	latitude=models.FloatField()
	longitude=models.FloatField()
	place_name=models.CharField(max_length=500)
	review=models.CharField(max_length=1000)