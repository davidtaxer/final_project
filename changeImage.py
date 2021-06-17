#!/usr/bin/env python3
import os
import sys
from PIL import Image

cwd = os.getcwd()
path = cwd + '/supplier-data/images/'
#new_path = '/supplier-data/images/'

#if not os.path.exists(new_path):
#    os.makedirs(new_path)

for files in os.listdir(path):
        print(files)
        if not files.startswith('.') and not files.startswith('README')and not files.startswith('LICENSE'):
            with Image.open(path + files) as im:
                im=im.convert('RGB').resize((600, 400))
                im=im.save(path + files, 'jpeg', quality=100)
