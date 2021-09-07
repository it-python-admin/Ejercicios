import urllib.request
webUrl  = urllib.request.urlopen('https://www.as.com')
data = webUrl.read()
data=str(data) #Convertimos los bytes recibidos en un string
print(type(data))
print(data.count("Real Madrid"))