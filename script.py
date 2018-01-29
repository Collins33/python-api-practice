from urllib.request import urlopen
import requests


#making a request to the website
kittens=urlopen("http://placekitten.com/")
response=kittens.read()

body=response[559:1000]

print(body)

#using the requests library
r=requests.get("http://www.google.com")

print(r)
