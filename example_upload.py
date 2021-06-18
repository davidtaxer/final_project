#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})


# moddified version of script
# #!/usr/bin/env python3
# import requests
# import os
# import sys
#
# cwd = os.getcwd()
# path = cwd + '/supplier-data/images/'
# url = "http://localhost/upload/"
#
# for image in os.listdir(path):
#         if image.endswith('.jpeg'):
#                 with open(path + image, 'rb') as opened:
#                    r = requests.post(url, files={'file': opened})
