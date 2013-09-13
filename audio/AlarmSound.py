from subprocess import call
from threading import Timer
from time import sleep

class AlarmSound:
	def __init__(self, delay=1):
		self.delay = delay

	def start_sound(self, url):
		def callback():
			print("CUNT")
			call(["mxplayer", url])
			self.timer = Timer(self.delay, callback)
			self.timer.start()
		callback()

	def play(self, url):
		self.start_sound(url)

	def stop(self):
		print("canceling")
		self.timer.cancel()

alarm_sound = AlarmSound(0.5)
alarm_sound.play("sound.wav")
alarm_sound.stop()
