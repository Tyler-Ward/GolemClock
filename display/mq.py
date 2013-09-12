import pika
from display import LCDLinearScroll

connection = pika.BlockingConnection(pika.ConnectionParameters(
	        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='screendisplay')

print ' [*] Waiting for messages. To exit press CTRL+C'

lcd_scroller =  LCDLinearScroll(())
def callback(ch, method, properties, body):
	lcd_scroller.display_message(body)


channel.basic_consume(callback, queue='screendisplay', no_ack=True)
channel.start_consuming()
