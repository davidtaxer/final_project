#!/usr/bin/env python3


import os
import requests

#get current working directory
cwd = os.getcwd()

#path to .txt files for this script
path = cwd + "/supplier-data/descriptions/"

# create a list of items in path
items = os.listdir(path)

# uncomment print line to check if items variable
# creats a list of files in path correctly

#print(items)

#itterate through files in the directory and store as a dictionary


for file in items:
        with open (path + file) as info:
                data = info.read().split('\n')
                file_dict = {'name':data[0], 'weight':data[1], 'description':data[2], "image_n$
                response = requests.post("http://34.69.160.243/fruits/", json=file_dict)
                print(response.status_code)


#print(list_of_files)
