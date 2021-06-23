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

# create a list of only the .jpeg files
jpeg_images = [image_name for image_name in image_files if '.jpeg' in image_name]

print('The following jpeg images will be used:')
print(sorted(jpeg_images))
print("")

# create a list of dictionaries of fruit with their information
list = []
for file in text_files:
    with open (description_path + file, 'r') as info:
        data = (info.read().split('\n'))
        file_dict = {'name':data[0], 'weight':int(data[1].split(" ")[0]), 'description':data[2]}
        list.append(file_dict)

    for image in jpeg_images:
        if image.split('.')[0] in file.split('.')[0]:
            file_dict['image_name']=image

print('The following descriptions will be uploaded:')
print(*list, sep = "\n" "\n")
print("")

#  Uploading the descriptions and images.
for item in list:
    resp = requests.post('http://34.134.195.119/fruits/', json=item)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))
