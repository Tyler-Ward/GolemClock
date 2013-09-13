import urllib2
import json

def get_routinfo(location0, location1, mode='driving'):
	url = 'http://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&mode={2}&sensor=false'.format(location0, location1, mode)
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return json.loads(response.read())

def routeinfo_message(location0, location1, mode='driving'):
	obj = get_routinfo(location0, location1, mode)
	msgs = []
	duration = obj['routes'][0]['legs'][0]['duration']
	msgs.append("Travel time: " +duration['text'])
	return {'type': 'routeinfo', 'messages': msgs, 'travel_time': duration}

print( routeinfo_message("SO172TH,UK", "Portsmouth,UK") )
