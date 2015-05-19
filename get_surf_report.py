#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
import decimal
import ConfigParser
import time

Config=ConfigParser.ConfigParser()
try:
    Config.read('/home/pi/alarmpi/alarm.config')
except:
    raise Exception('Sorry, Failed reading alarm.config file.')

try:

    hour = time.strftime("%H")

    num = int(hour)

    surf_api = urllib.urlopen("http://www.spitcast.com/api/spot/forecast/204/")
    response = surf_api.read()
    response_dictionary = json.loads(response)

    data = response_dictionary[num]

    location = data['spot_name']
    date = data['date']
    hour = data['hour']
    size = data['size']
    shape = data['shape_full']

    if '-' in shape:
       newshape = shape.replace('-', ' to ')
    else:
        newshape = shape

    msg = "Good Morning. This is the surf report for " + str(location) + " on " + str(date) + " at "+ str(hour) +"."+ " The surf is " + str(size) +" feet and the shape is "+ newshape +"."

    tide_api = urllib.urlopen('http://api.spitcast.com/api/county/tide/los-angeles/')
    tide_response = tide_api.read()
    response_dictionary_tide = json.loads(tide_response)

    current_tide = response_dictionary_tide[num].get('tide')

    next_tide = response_dictionary_tide[num+1]['tide']

    direction = "dropping"

    if int(next_tide) > int(current_tide):
        direction = "rising"

    format_tide = round(current_tide,2)

    tide = " The tide is "+ str(format_tide)+ " feet and "+ direction + "."

    surf_report_raw = msg + tide

    surf_report = " "

    x = 1
    while x < 10:
        surf_report = surf_report + surf_report_raw
        x += 1

except Exception:
    surf = 'Failed to connect to Surf Report.  '

if Config.get('main','debug') == str(1):
    print surf_report

    