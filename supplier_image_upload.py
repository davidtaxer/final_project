#!/usr/bin/env python3
import requests
import os

cwd = os.getcwd()
path = cwd + '/supplier-data/images/'
url = "http://localhost/upload/"

for image in os.listdir(path):
        if image.endswith('.jpeg'):
                with open(path + image, 'rb') as opened:
                   r = requests.post(url, files={'file': opened})
