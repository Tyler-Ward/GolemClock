import urllib2
import json
import sqlite3

def get_weather(city, country):
	url = "http://api.openweathermap.org/data/2.5/weather?q={0},{1}".format(city, country)
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return json.loads(response.read())


def weather_message(city, country):
	obj = get_weather(city, country)
	msgs = []
	if obj['weather'][0]['main'] == u'Rain':
		msgs.append("Chance of rain")
	if obj['weather'][0]['main'] ==  u'Snow':
		msgs.append("Chance of snow")	
	return {'type': 'weather', 'messages': msgs, 'possible_delays': True}

connection = sqlite3.connect("/home/pi/GolemClock/webface/golem.db")

def add_module_db():
	with connection:
		cursor = connection.cursor()
		cursor.execute("INSERT INTO golem_module (module_name, enabled) VALUES ('weather', 1);")


def read_module_db():
	with connection:
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM golem_module;")
		return cursor.fetchall()

def read_offset_db():
	with connection:
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM golem_offset;")
		return cursor.fetchall()

def read_alarm_db():
	with connection:
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM golem_offset;")
		return cursor.fetchall()

print(read_alarm_db())
