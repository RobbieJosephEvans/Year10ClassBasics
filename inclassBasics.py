import requests

myrequest = requests.get("https://geo-info.co/43,-81")

datajson = myrequest.json()

ofile = open("destroyme/html","w")
ofile.write("<h1>" + datajson["city"] + "</h1>")
ofile.close()
