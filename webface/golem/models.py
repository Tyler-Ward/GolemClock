from django.db import models

# Create your models here.

class Alarm(models.Model):
	time = models.DateTimeField()
	mondays = models.BooleanField(blank=True)
	tuesdays = models.BooleanField(blank=True)
	wednesdays = models.BooleanField(blank=True)
	thursdays = models.BooleanField(blank=True)
	fridays = models.BooleanField(blank=True)
	saturdays = models.BooleanField(blank=True)
	sundays = models.BooleanField(blank=True)
	
	activated = models.BooleanField(default=True)
	suppressed = models.BooleanField(default=False)

