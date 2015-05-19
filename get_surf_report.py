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
    surf_api = urllib.urlopen("http://www.spitcast.com/api/spot/forecast/204/")
    response = surf_api.read()
    response_dictionary = json.loads(response)

    location = response_dictionary[7]['spot_name']
    date = response_dictionary[7]['date']
    hour = response_dictionary[7]['hour']
    size = response_dictionary[7]['size']
    shape = response_dictionary[7]['shape_full']


    msg = "This is the surf report for " + str(location) + " on " + str(date) + " at "+ str(hour) +"."+ " The surf is " + str(size) +" feet and the shape is "+ str(shape) +"."

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

    # current = response_dictionary['query']['results']['channel']['item']['condition']['temp']
    # current_low = response_dictionary['query']['results']['channel']['item']['forecast'][0]['low']
    # current_high = response_dictionary['query']['results']['channel']['item']['forecast'][0]['high']
    # conditions = response_dictionary['query']['results']['channel']['item']['condition']['text']
    # forecast_conditions = response_dictionary['query']['results']['channel']['item']['forecast'][0]['text']
    # wind = response_dictionary['query']['results']['channel']['wind']['speed']
    # wind_chill = response_dictionary['query']['results']['channel']['wind']['chill']
    # sunrise = response_dictionary['query']['results']['channel']['astronomy']['sunrise']
    # sunset = response_dictionary['query']['results']['channel']['astronomy']['sunset']



    # if wind != '':
    #   print response_dictionary ['query']['results']['channel']['wind']['speed']
    #   wind = round(float(wind),1)

#    print current
#    print current_low
#    print current_high
#    print conditions
#    print wind


#     if conditions != forecast_conditions:
#         conditions = conditions + ' becoming ' + forecast_conditions 
#     weather_yahoo = 'Weather for today is ' + str(conditions) + ' currently ' + str(current) + ' degrees with a low of ' + str(current_low) + ' and a high of ' + str(current_high) + '.  '

# # Wind uses the Beaufort scale
#     if Config.get('weather_yahoo','metric') == str(1) and Config.get('weather_yahoo','wind') == str(1):
#         if wind < 1:
#             gust = 'It is calm'
#         if wind > 1:
#             gust = 'With Light Air'
#         if wind > 5:
#             gust = 'With a light breeze'
#         if wind > 12:
#             gust = 'With a gentle breeze'
#         if wind > 20:
#             gust = 'With a moderate breeze'
#         if wind > 29:
#             gust = 'With a fresh breeze'
#         if wind > 39:
#             gust = 'With a strong breeze'
#         if wind > 50:
#             gust = 'With High winds at ' + wind + 'kilometres per hour'
#         if wind > 62:
#             gust = 'With Gale force winds at ' + wind + 'kilometres per hour'
#         if wind > 75:
#             gust = 'With a strong gale at ' + wind + 'kilometres per hour'
#         if wind > 89:
#             gust = 'With Storm winds at ' + wind + 'kilometres per hour'
#         if wind > 103:
#             gust = 'With Violent storm winds at ' + wind + 'kilometres per hour'
#         if wind > 118:
#             gust = 'With Hurricane force winds at ' + wind + 'kilometres per hour'
#         if wind == '':
#             gust = ''
#         weather_yahoo = weather_yahoo + str(gust) + '.  '

#     if Config.get('weather_yahoo','wind_chill') == str(1) and wind > 5 and int(time.strftime("%m")) < 4 or wind > 5 and int(time.strftime("%m")) > 10:
#         weather_yahoo = weather_yahoo + ' And a windchill of ' + str(wind_chill) + '.  '

except Exception:
    surf = 'Failed to connect to Surf Report.  '

if Config.get('main','debug') == str(1):
  print surf_report