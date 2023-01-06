import requests
from lxml.html import document_fromstring


r = requests.get("https://www.python.org/downloads/")

print(document_fromstring(r.text).find_class("download-list-widget"))
