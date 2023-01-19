import requests
from lxml.html import document_fromstring


element = requests.get("https://www.python.org/downloads/")

releases = document_fromstring(element.text).find_class("release-number")

#releases = document_fromstring(element.text).find_class("release-download")

for i in range(1,len(releases)):
   print(releases[i].getchildren()[0].text_content())
   
   #https://www.python.org/ftp/python/3.8.12/
    
   #print("https://www.python.org" + releases[i].getchildren()[0].get("href"))
    
    # [0].get("href")