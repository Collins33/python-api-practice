#!/usr/bin/env python
import urllib2
import json
from credentials import *
from Broadcast import Broadcast




def getNews(category):

    news_list=[]
    news_url="https://newsapi.org/v2/everything?q="+str(category)+"&sortBy=publishedAt&apiKey=" +str(news_api)
    json_object=urllib2.urlopen(news_url)#using urllib urlopen method to open the url

    data= json.load(json_object)#turn the response into json


    for news in data['articles']:
        title=news["title"]
        description=news["description"]
        url=news["url"]
        habari=Broadcast(title,description,url)
        news_list.append(habari)
    print(news_list[0].title)    



getNews("politics")

