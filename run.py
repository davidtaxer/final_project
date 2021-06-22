#!/usr/bin/env python3


import os
import requests

#get current working directory
cwd = os.getcwd()

# paths to description files and images
description_path = cwd + "/supplier-data/descriptions/"
image_path = cwd + "/supplier-data/images/"

# create a list of descriptions
text_files = os.listdir(description_path)
image_files = os.listdir(image_path)
# uncomment print line to check if items variable
# creats a list of files in path correctly

# print(items)
# print(images)
#itterate through files in the directory and store as a dictionary
list = []
for file in text_files:
        with open (description_path + file, 'r') as info:
            data = (info.read().split('\n'))
            file_dict = {'name':data[0], 'weight':int(data[1].split(" ")[0]), 'description':data[2]}
            list.append(file_dict)
#            response = requests.post("http://34.69.160.243/fruits/", json=file_dict)
#            print(response.status_code)

for image in image_files:
    if image.split('.')[0] in file.split('.')[0]:
        file_dict['image_name']=image
    list.append(file_dict)

for item in list:
    resp = requests.post('http://34.134.195.119/fruits/', json=item)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))

#print(*list, sep = "\n")
