#!/usr/bin/env python
import urllib2
import json
from credentials import *




json_object=urllib2.urlopen(news_url)

data= json.load(json_object)

print(data)