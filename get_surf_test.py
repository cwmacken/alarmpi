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

print msg
