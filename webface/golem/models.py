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
	manual = models.BooleanField(default=True)

class Module(models.Model):
	module_name = models.CharField(max_length=50)
	enabled = models.BooleanField(default=True)

class Information(models.Model):
	module_id = models.ForeignKey(Module)
	short_text = models.CharField(max_length=100)
	long_text = models.CharField(max_length=1000)


class Offset(models.Model):
	alarm_id = models.ForeignKey(Alarm)
	module_id = models.ForeignKey(Module)
	offset = models.IntegerField() #signed offset in seconds -= earler +=later
	short_reason = models.CharField(max_length=100)
	long_reason = models.CharField(max_length=1000)
	

