import os
import sys
import json

class CustomException(Exception):
   pass
 
def getCurrentDir(path):
    return path[path.rindex("\\")+1:len(path)]

def getExt(file):
    return file[file.rindex(".")+1:len(file)]

# Assume there is only one json file
if (len(sys.argv)-1 != 2): raise CustomException("Wrong number of arguments (expected 2, got " + str(len(sys.argv)-1) + ")")
SCRIPT_NAME, RAW_DATA_RELEASE_PATH, TEMP_DATA_PATH = sys.argv

if not os.path.isdir(TEMP_DATA_PATH): os.makedirs(TEMP_DATA_PATH)
with open(TEMP_DATA_PATH + "\\benchmarks.csv", "a") as benchmark_data:
    benchmark_data.write("Benchmarks,Mean (s),Standard Deviation (s),Coefficient of Variance\n")

    for root, dirs, files in os.walk(RAW_DATA_RELEASE_PATH):
        if len(files):
            benchmark = getCurrentDir(root)
            jsonFile = ""
            
            for f in files:
                if getExt(f) == "json": 
                    jsonFile = f
                    break
            with open(root + "\\" + jsonFile, "r") as jFile:
                text = jFile.read()
                if (len(text)):

                    contents = text.replace("\\", "\\\\\\")
                    file_dict = json.loads(contents)["results"][0]
                    benchmark_data.write(benchmark + "," + str(file_dict["mean"]) + "," + str(file_dict["stddev"]) + "," + "\n")
                 
                # incompatible
                else: 
                    benchmark_data.write(benchmark + ",N/A,N/A,N/A\n")
                    