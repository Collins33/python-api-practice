from urllib.request import urlopen

kittens=urlopen("http://placekitten.com/")
response=kittens.read()

body=response[559:1000]

print(body)
