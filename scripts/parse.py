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
SCRIPT_NAME, RAW_DATA_PATH, TEMP_DATA_PATH = sys.argv

if not os.path.isdir(TEMP_DATA_PATH): os.makedirs(TEMP_DATA_PATH)

with open(TEMP_DATA_PATH + "\\releases.csv", "a") as release_data:
    release_data.write(",Bounce,DeltaBlue,Json,List,Permute,Queens,Sieve,Storage,Towers\n")

    for outer_root, outer_dirs, outer_files in os.walk(RAW_DATA_PATH):
        if (len(outer_dirs) == 9):
            release = getCurrentDir(outer_root)
            print(release)
            release_data.write(release + ",")
            for benchmark in outer_dirs:
                for root, dirs, files in os.walk(RAW_DATA_PATH + "\\" + release + "\\" + benchmark):

                    if len(files):
                        benchmark = getCurrentDir(root)
                        jsonFile = ""
                        
                        for f in files:
                            if getExt(f) == "json": 
                                jsonFile = f
                                break
                        # print(root + "\\" + jsonFile)
                        with open(root + "\\" + jsonFile, "r") as jFile:
                            text = jFile.read()
                            if (len(text)):

                                contents = text.replace("\\", "\\\\\\")
                                file_dict = json.loads(contents)["results"][0]
                                # print(str(file_dict["mean"]))
                                release_data.write(str(file_dict["mean"])+",")
                             
                            ##incompatible
                            else: 
                                release_data.write("N/A,"*9)
                                
            release_data.write("\n")
                                