#!/usr/bin/python

import alarmlogic
import pika
import threading
import time

alarmlist=[]
running =True

alarmstatus="OFF"
#alarm modes
# OFF alarm is off
# ON alarm is on
# CANCLED alarm has been cancled
#
#
#
#

snoozeactive=False
# SNOOZE alarm is in snooze mode
snoozetime=alarmlogic.snoozealarm

# performs time based actions
def timethread():

	while running:
		alarm_set = alarmlogic.evaluatealarms(alarmlist)

		if alarm_set == 1 and alarmstatus=="OFF":
			channel.basic_publish(exchange='clock_output',
	                routing_key='',
	                body='ALARM_START')
		        alarmastatus="ON"
 		elif alarm_set == 0 and alarmastatus=="ON":
 			channel.basic_publish(exchange='clock_output',
        	        routing_key='',
        	        body='ALARM_STOP')
        	        alarmstatus="OFF"
		elif alarm_set ==0 and alarmstatus=="CANCLED":
			alarmstatus="OFF"
			snoozetime=False
	
		time.sleep(1)
        	alarmlist = alarmlogic.getalarms()
		if snoozeactive:
			alarmlist.append(snoozetime)


def processcommand(ch, method, properties, body):
	print " [x] Received %r" % (body,)

	if body == "ALARM_CANCEL" or body == "alarm_cancel":
		channel.basic_publish(exchange='clock_output',
			routing_key='',
			body='ALARM_STOP')
		alarmstatus="CANCLED"
	elif body == "ALARM_SNOOZE" or body == "alarm_snooze":
		channel.basic_publish(exchange='clock_output',
			routing_key='',
			body='ALARM_STOP')
		alarmstatus="CANCLED"
		snoozeactive=True
		#add alarm event for snooze
		snoozetime.time=time.time()+(60*3)
	else:
		print "unrecognised command"	




if __name__ == "__main__":

        connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))
        channel = connection.channel()

#        channel.queue_declare(queue='output')

	# input channels
	channel.queue_declare(queue='commands')

	# output channels
	channel.exchange_declare(exchange='clock_output',type='fanout')

        alarmlist = alarmlogic.getalarms()

	t1 = threading.Thread(target=timethread)
	t1.start()

	try:
		channel.basic_consume(processcommand,
                      queue='commands',
                      no_ack=True)
		channel.start_consuming()

	except KeyboardInterrupt:
		running=False

