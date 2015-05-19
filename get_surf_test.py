import urllib
import urllib2
import json
import decimal
import ConfigParser
import time

surf_api = urllib.urlopen("http://www.spitcast.com/api/spot/forecast/204/")
response = surf_api.read()
response_dictionary = json.loads(response)

location = response_dictionary[7]['spot_name']
date = response_dictionary[7]['date']
hour = response_dictionary[7]['hour']
size = response_dictionary[7]['size']
shape = response_dictionary[7]['shape_full']


msg = "Good Morning. This is the surf report for " + str(location) + " on " + str(date) + " at "+ str(hour) +"."+ " The surf is " + str(size) +" feet and the shape is "+ str(shape) +"."

tide_api = urllib.urlopen('http://api.spitcast.com/api/county/tide/los-angeles/')
tide_response = tide_api.read()
response_dictionary_tide = json.loads(tide_response)

current_tide = response_dictionary_tide[7]['tide']

next_tide = response_dictionary_tide[8]['tide']

direction = "dropping"

if next_tide > current_tide:
	direction = "rising"

format_tide = round(current_tide,2)

tide = " The tide is "+ str(format_tide)+ " feet and "+ direction + "."

surf_report = msg + tide

print surf_report
