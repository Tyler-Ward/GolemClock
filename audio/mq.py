import pika
import pickle
from display import LCDLinearScroll
from AlarmSound import AlarmSound

connection = pika.BlockingConnection(pika.ConnectionParameters(
	        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='screendisplay')

print ' [*] Waiting for messages. To exit press CTRL+C'

alarm_sound = AlarmSound(0.5)
def callback(ch, method, properties, body):
	print("message received: {0}".format(body))	
	alarm_sound.play("sound.wav")
	

channel.basic_consume(callback, queue='screendisplay', no_ack=True)
channel.start_consuming()
