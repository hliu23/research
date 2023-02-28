import requests
from lxml.html import document_fromstring
import shutil
import os

class CustomException(Exception):
  pass

def download(url, file, dir):
   ext = url[len(url)-3:]
   with requests.get(url, stream=True) as res:
      with open(os.path.join(dir, file + "." + ext), "wb") as f:
        shutil.copyfileobj(res.raw, f)

element = requests.get("https://nodejs.org/en/download/releases/")

with open("C:\\Users\\codin\\Documents\\personal\\projects\\research\\data\\temp\\releases.txt", "r") as releases:
  lines = releases.readlines()
  for line in lines:
    release = line.strip("\n")
    download("https://nodejs.org/download/release/v" + release + "/node-v" + release + "-x86.msi", release, "C:\\Users\\codin\\Documents\\personal\\projects\\research\\new")

# 