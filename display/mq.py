import pika
import pickle
from display import LCDLinearScroll

connection = pika.BlockingConnection(pika.ConnectionParameters(
	        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='screendisplay')
channel.queue_declare(queue='output')

print ' [*] Waiting for messages. To exit press CTRL+C'

def select_callback():
	channel.basic_publish(exchange='clock_output', routing_key='', body='ALARM_STOP')
	channel.basic_publish(exchange='clock_output', routing_key='', body='ALARM_CANCEL')


def callback(ch, method, properties, body):
	print("message received: {0}".format(body))
	items = pickle.loads(body)
	if len(items) != 0:
		lcd_scroller =  LCDLinearScroll(items, select_callback=select_callback)
		lcd_scroller.display_message("Scroll through\nmessages")
		lcd_scroller.setup_scroll_events()


channel.basic_consume(callback, queue='screendisplay', no_ack=True)
channel.start_consuming()
