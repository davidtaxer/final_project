#!/usr/bin/env python3


import os
import requests

#get current working directory
cwd = os.getcwd()

# paths to description files and images
description_path = cwd + "/supplier-data/descriptions/"
image_path = cwd + "/supplier-data/images/"

# create a list of descriptions
items = os.listdir(description_path)

# uncomment print line to check if items variable
# creats a list of files in path correctly

#print(items)

#itterate through files in the directory and store as a dictionary

for file in items:
        data = []
        with open (description_path + file) as info:
                data = info.read().split('\n')
                file_dict = {'name':data[0], 'weight':data[1], 'description':data[2], "image_name":data[3]}
#                response = requests.post("http://34.69.160.243/fruits/", json=file_dict)
#                print(response.status_code)


print(data)
