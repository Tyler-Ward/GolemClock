import pika
import pickle
from display import LCDLinearScroll

connection = pika.BlockingConnection(pika.ConnectionParameters(
	        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='clock_output', type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='clock_output', queue=queue_name)

print ' [*] Waiting for messages. To exit press CTRL+C'

def select_callback():
	print("select message sent")	
	channel.basic_publish(exchange='clock_output', routing_key='', body='ALARM_STOP')
	channel.basic_publish(exchange='clock_output', routing_key='', body='ALARM_CANCEL')


def callback(ch, method, properties, body):
	print("message received: {0}".format(body))
	if body == "ALARM_START":
		items = ("It's sunny today", "Meeting at 2pm")
		lcd_scroller =  LCDLinearScroll(items, select_callback=select_callback)
		lcd_scroller.display_message("Scroll through\nmessages")
		#lcd_scroller.setup_scroll_events()

channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()
