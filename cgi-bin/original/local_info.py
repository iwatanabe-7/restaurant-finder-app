#!/usr/bin/env python3

import requests

cur_location = requests.get("https://get.geojs.io/v1/ip/geo.json").json()
print("緯度:" + cur_location['latitude'])
print("経度:" + cur_location['longitude'])

with open('./view/local_info.html', 'r', encoding='utf-8') as template_file:
    template = template_file.read()

result = template.format(lat=cur_location['latitude'], lng=cur_location['longitude'])
print("Content-Type: text/html; charset=utf-8\n")
print(result)