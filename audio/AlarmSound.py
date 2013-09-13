from subprocess import Popen
from threading import Timer
from time import sleep

class AlarmSound:
	def __init__(self, delay=1):
		self.delay = delay
		self.started = False

	def start_sound(self, url):
		callback()

	def play(self, url):
		if not self.started:
			self.process = Popen(["mplayer", url, "-loop", "0"])
			self.started = True

	def stop(self):
		print("canceling")
		self.process.kill()
		self.started = False

#alarm_sound = AlarmSound(0.5)
#alarm_sound.play("sound.wav")
#alarm_sound.stop()
