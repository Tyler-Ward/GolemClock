import pika
import pickle
from display import LCDLinearScroll

connection = pika.BlockingConnection(pika.ConnectionParameters(
	        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='screendisplay')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
	print("message received: {0}".format(body))
	items = pickle.loads(body)
	if len(items) != 0:
		lcd_scroller =  LCDLinearScroll(items)
		lcd_scroller.display_message("Scroll through\nmessages")
		lcd_scroller.setup_scroll_events()


channel.basic_consume(callback, queue='screendisplay', no_ack=True)
channel.start_consuming()
