import urllib2
import json

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

print( weather_message("Southampton", "UK") )
