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


    for news in data['articles']:#loop through the response
        #get the title,description and url
        title=news["title"]
        description=news["description"]
        url=news["url"]
        #build the object 
        habari=Broadcast(title,description,url)
        #append the object into the empty list
        news_list.append(habari)

    # loop through the list with news objects and print the news title
    for x in range(0,len(news_list)):
        print(news_list[x].title)
        print(news_list[x].description)
        print("                       ")    



getNews("politics")

