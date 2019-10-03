import requests

myrequest = requests.get("https://geo-info.co/43,-79")
datajson = myrequest.json() #turns myrequests (which is in binary) into a json file

city = datajson["city"] #becomes string

nearby = datajson["nearbyCities"] #becomes list (because there is data underneath) of everything under it

forterie = nearby[2]["city"]


ofile = open("testing.html","w") #open function deals with files and was three modes;
#"w" (write), "a" (append), and "r" (read only)
ofile.write("<h1>" + city + "</h1>")
ofile.write("<p>" + forterie + "</p>")
ofile.close()
