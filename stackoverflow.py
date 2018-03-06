import requests
request = requests.get("https://drive.google.com/uc?export=download&id=0B6ZlG_Eygdj-c1kzcmUxN05VUXM")
file = open("survey2017.zip", "wb")
file.write(request.content)
file.close()

import zipfile
zip = zipfile.ZipFile("survey2017.zip", "r")
zip.extractall("survey2017")
zip.close()

import shutil
shutil.move("survey2017/survey_results_public.csv", "survey2017.csv")
shutil.rmtree("survey2017")

import os
os.remove("survey2017.zip")




print("Hello world!")
