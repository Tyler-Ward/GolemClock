import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='commands')
channel.queue_declare(queue='screendisplay')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    channel.basic_publish(exchange='',
                          routing_key='screendisplay',
                          body=body)
    

channel.basic_consume(callback,
                      queue='commands',
                      no_ack=True)

channel.start_consuming()
