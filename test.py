# first
import uuid
import requests
import numpy as np
import cv2

import os
from os.path import exists, join, basename, splitext, abspath

# second
import sys
sys.path.append(join('mongolian-nlp', 'image2bichig'))
if True:
    from ocr import line_segmentation, ocr
checkpoint_file_name = 'image2bichig-checkpoint.pth'


def clear_text(text):
    res = ''
    for i in range(len(text)):
        if (ord(text[i]) == 32):
            res += ' '
        if (ord(text[i]) == 6145):
            res += text[i]
        elif (ord(text[i]) < 6314 and ord(text[i]) > 6160):
            res += text[i]
        elif (ord(text[i]) < 1000):
            res += text[i]
    return res


img = cv2.imread('./images/T-Purevdorj-2.PNG', 0)
lines = line_segmentation(img, aspect_ratio=0.25)
img_copy = img.copy()
for line in lines:
    (x1, y1), (x2, y2) = line
    cv2.rectangle(img_copy, (x1, y1), (x2, y2), 0, 3)

texts = ''
for line_img, line_txt in ocr(img, lines, checkpoint_file_name):
    texts += line_txt + ' '

test = clear_text(texts)

# Add your key and endpoint
key = "f29916616c674002a39d451db4e9ad1d"
endpoint = "https://api.cognitive.microsofttranslator.com/"
location = "eastasia"
path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'mn-Mong',
    'to': ['mn-Cyrl'],
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': test
}]

request = requests.post(constructed_url, params=params,
                        headers=headers, json=body)
response = request.json()
res = response[0]['translations'][0]['text']
print(res)
