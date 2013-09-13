import pika
import pickle
from AlarmSound import AlarmSound

connection = pika.BlockingConnection(pika.ConnectionParameters(
	        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='output')

print ' [*] Waiting for messages. To exit press CTRL+C'

alarm_sound = AlarmSound(0.5)
def callback(ch, method, properties, body):
	print("message received: {0}".format(body))	
	if body == "ALARM_START":
		alarm_sound.play("sound.wav")
	elif body == "ALARM_STOP":
		alarm_sound.stop()
	

channel.basic_consume(callback, queue='output', no_ack=True)
channel.start_consuming()
