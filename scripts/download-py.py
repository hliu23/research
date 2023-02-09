import sys
import requests
import shutil
import os
import re
from lxml.html import document_fromstring


class CustomException(Exception):
   pass

def checkDir(dirList):
   for dir in dirList:
      if not os.path.isdir(dir): os.makedirs(dir)

def format_date(string):
   match = re.search("(?P<month>[A-Za-z.]+) (?P<day>[0-9]+), (?P<year>[0-9]+)", string)
   months = { "Jan.": 1, "Feb.": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "Aug.": 8, "Sept.": 9, "Oct.": 10, "Nov.": 11, "Dec.": 12 }
   return (str(months[match.group("month")]) + "/" + match.group("day") + "/" + match.group("year"))

# dir needs to exist
def download(url, file, dir):
   ext = url[len(url)-3:]
   with requests.get(url, stream=True) as res:
      with open(os.path.join(dir, file + "." + ext), "wb") as f:
         shutil.copyfileobj(res.raw, f)


class Release:
   url_formats = ["https://www.python.org/ftp/python/***/python-***-amd64.exe", "https://www.python.org/ftp/python/***/python-***.amd64.msi", "https://www.python.org/ftp/python/***/python-***.msi", "https://www.python.org/ftp/python/***/Python-***.exe"]
   url_version = 0

   def __init__(self, tag):
      self.tag = tag
      self.url = self.find_url()
      self.end_with_zero = False

   def format_tag(self):
      # no zero at the end of tag
      if (self.tag[len(self.tag)-1:] == "0"):
         mod_tag = self.tag[:len(self.tag)-2]
         self.end_with_zero = True
      else: mod_tag = self.tag
      return mod_tag
   
   def in_range(self):
   #    last_versions = ["3.9.13", "3.8.10", "3.7.9", "3.6.8", "3.5.4", "3.4.4", "3.3.5", "3.2.5", "3.1.4", "3.0.1", "2.7.18", "2.6.6", "2.5.4", "2.4.4", "2.3.5", "2.2.3", "2.1.3", "2.0.1"]
      last_versions = [[], [], [1, 3, 3, 5, 4, 4, 6, 18], [1, 4, 5, 5, 4, 4, 8, 9, 10, 13]]
      tag_val = [int(num) for num in self.tag.split(".")]
      ver = tag_val[2]
      try:
         last_ver = last_versions[tag_val[0]][tag_val[1]]
      except IndexError:
         return "N/A"
      return (ver <= last_ver)

   def find_url(self):
      def find_next(current):
         arr = Release.url_formats
         if (current > len(arr)-1): raise CustomException("Index number of url_formats out of range")
         elif (current == len(arr)-1): return 0
         else: return current + 1
      
      def get_url(url_version, tag):
         return Release.url_formats[url_version].replace("***", tag)

      def test_url(url):
         status = requests.get(url).status_code
         return (status == 200)

      def test(tag):
         testing_index = Release.url_version

         for i in range(0, len(Release.url_formats)):
            if i > 0: testing_index = find_next(testing_index)
            url = get_url(testing_index, tag)

            if (test_url(url)): 
               Release.url_version = testing_index
               return url
         return "N/A"

      if (self.in_range() or self.in_range() == "N/A"):
         res = test(self.tag)
         if (res != "N/A"): return res
         if self.end_with_zero: return test(self.format_tag())

      return "N/A"
      # raise CustomException("No working url found for release " + self.format_tag())

# main

print("Preparing data files...")
if (len(sys.argv)-1 != 4): raise CustomException("Wrong number of arguments (expected 4, got " + str(len(sys.argv)-1) + ")")
SCRIPT_NAME, RAW_DATA_PATH, TEMP_DATA_PATH, COMPILED_DATA_PATH, DOWNLOAD_PATH = sys.argv
checkDir([RAW_DATA_PATH, TEMP_DATA_PATH, DOWNLOAD_PATH])

release_data_file = RAW_DATA_PATH + "\\releases.csv"
temp_reference_file = TEMP_DATA_PATH + "\\releases.txt"
delete = input("Delete existing data? (y/n) ")
if delete == "y": 
   # make sure the file is not opened somewhere else
   os.remove(release_data_file)
   os.remove(temp_reference_file)


print("Retrieving release tags from https://www.python.org/downloads/...")
element = requests.get("https://www.python.org/downloads/")
tags = document_fromstring(element.text).find_class("release-number")
dates = document_fromstring(element.text).find_class("release-date")
if len(tags) != len(dates): raise CustomException("Release dates do not match release numbers")

with open(release_data_file, "a") as release_data:
   with open(temp_reference_file, "a") as temp_reference:
      for i in range(1, len(tags)):
         tag = tags[i].getchildren()[0].text_content()[7:]
         date = dates[i].text_content()

         print("Checking release " + tag + "...")
         release = Release(tag)
         release_data.write(tag + "," + format_date(date) + "," + release.url + "\n")
         if (release.url != "N/A"): 
            temp_reference.write(release.tag + "\n")
            download(release.url, release.tag, DOWNLOAD_PATH)
            print("Successfully downloaded release " + tag)
