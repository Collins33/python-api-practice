#!/usr/bin/env python
import urllib2
import json
from credentials import *



news_url="https://newsapi.org/v2/everything?q=health&sortBy=publishedAt&apiKey=" +str(news_api)
json_object=urllib2.urlopen(news_url)#using urllib urlopen method to open the url

data= json.load(json_object)#turn the response into json


for news in data['articles']:
    print (news["description"])
