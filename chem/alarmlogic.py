#!/usr/bin/python

import time
import sqlite3

testalarm = {
"id" : 1,
"time" : time.time(),
"mondays" : True,
"tuesdays" : True,
"wednesdays" : True,
"thursdays" : True,
"fridays" : True,
"saturdays" : True,
"sundays" : True,
"activated" : True,
"suppressed" : False
}

dayname = (time.strftime('%A')+"s").lower()

def clearsuppressed(alarmid):
	print "clear surppressed flag on ", alarmid

def check_fire_time(alarmtime):
	alarmtime = alarmtime % 86400
	timenow = time.time() % 86400
	#print alarmtime,timenow
	if alarmtime < timenow+30 and alarmtime > timenow-30:
		return True
	else:
		return False

def should_fire_alarm(alarm):
	#check if alarm is activated
	if (alarm['activated'] == True) and (alarm[dayname] == True) and check_fire_time(alarm['time']):
		if alarm['suppressed'] == True:
			clearsuppressed(alarm[id])
			return False
		else:
			return True
	else:
		return False


def getalarms():

	conn = sqlite3.connect('../webface/golem.db')
	c = conn.cursor()
	alarmlist=[]
	
	for row in c.execute('SELECT * FROM golem_alarm'):
		#print row
		#print type(row[2]==1)
		timevalue = time.mktime(time.strptime(row[1],"%Y-%m-%d %H:%M:%S"))
		alarmlist.append({'id':row[0],
		'time':timevalue,
		"mondays" : (row[2]==1),
		"tuesdays" : (row[3]==1),
		"wednesdays" : (row[4]==1),
		"thursdays" : (row[5]==1),
		"fridays" : (row[6]==1),
		"saturdays" : (row[7]==1),
		"sundays" : (row[8]==1),
		"activated" : (row[9]==1),
		"suppressed" : (row[10]==1)})

	conn.close()
	
	return alarmlist

def evaluatealarms(alarmlist):

	alarm_set=0	

	#print alarmlist
	for alarmentry in alarmlist:
		if should_fire_alarm(alarmentry):
			alarm_set=1
			#print "ALARM ALARM ALARM"

	return alarm_set


if __name__ == "__main__":
	import pika


	connection = pika.BlockingConnection(pika.ConnectionParameters(
        	host='localhost'))
	channel = connection.channel()

	channel.queue_declare(queue='output')

	alarmactive=0

	while(1):
		alarmlist = getalarms()
		alarm_set = evaluatealarms(alarmlist)
	

		if alarm_set == 1 and alarmactive==0:
			channel.basic_publish(exchange='',
			routing_key='output',
			body='ALARM_START')
			alarmactive=1
		elif alarm_set == 0 and alarmactive==1:
			channel.basic_publish(exchange='',
	                routing_key='output',
	                body='ALARM_STOP')
			alarmactive=0



	time.sleep(1)	
