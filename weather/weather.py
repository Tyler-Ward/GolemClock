import urllib2
import json

def get_weather(city, country):
	url = "http://api.openweathermap.org/data/2.5/weather?q={0},{1}".format(city, country)
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return json.loads(response.read())

print( get_weather("Southampton", "UK") )
