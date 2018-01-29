import requests

body={"name":"eric","age":"26"}

#make post request using requests library

requests.post("http://codecademy.com/learn-http/",data=body)
