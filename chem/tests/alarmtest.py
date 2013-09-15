#!/usr/bin/python

import alarmlogic
import pika
import time

if __name__ == "__main__":

        connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='output')

	channel.exchange_declare(exchange='clock_output',type='fanout')


	channel.basic_publish(exchange='clock_output',
	routing_key='',
	body='ALARM_START')

	time.sleep(10)

	channel.basic_publish(exchange='clock_output',
	routing_key='',
	body='ALARM_STOP')

