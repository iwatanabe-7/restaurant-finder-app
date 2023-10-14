#!/usr/bin/env python3

import os
import requests
import json
import cgi
import html
import io
import sys
from dotenv import load_dotenv
import random

load_dotenv()

form = cgi.FieldStorage()
form_address = form.getvalue('address',"")
form_lunch = form.getvalue('lunch',"0")
form_keyword = form.getvalue('keyword',"")
form_lat = form.getvalue('lat',"")
form_lng = form.getvalue('lng',"")
form_shuffle = form.getvalue('shuffle',"true")
api_key = (os.environ['API_KEY'])

access = ""
address = ""
hp = ""
coupon = ""
tmp=""
template = """"""

response = requests.get(
    'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/',
    params={'key': api_key,
        'address': form_address,
        'lunch': form_lunch,
        'keyword': form_keyword,
        'lat': form_lat,
        'lng': form_lng,
        'range': '5',
        'order': '4',
        'count': '100',
        'format': 'json'
    }
)

list = json.loads(response.text)["results"]["shop"]

if form_shuffle:
    random.shuffle(list)

for i, e in enumerate(list):
    name = e["name"]
    access = e["access"]
    time = e["open"]
    close_day = e["close"]
    hp = e["urls"]["pc"]
    coupon = e["coupon_urls"]["sp"]
    img = e["photo"]["pc"]["l"]

    tmp += f"""
        <div class="card mt-3" style="height: 15rem">
            <div id={i}>
                <div class="row g-0">
                    <div class="col-md-4">
                        <img src={img} class="card-img-left" alt="検索したお店">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body overflow-auto" style="height: 15rem">
                            <div class="card-text overflow-auto">
                                <h5 class="card-title">{name}</h5>
                                <p><i class="bi bi-geo-alt"></i> {access}</p>
                                <p><i class="bi bi-clock"></i> {time}</p>
                                <a href="{hp}"><i class="bi bi-file-earmark-fill"></i>ホームページ</a>
                                <a href="{coupon}">クーポン</a>
                                <div class="position-absolute bottom-0 start-50 translate-middle">
                                    
                                </div>
                                <div class="position-absolute bottom-0 end-0">
                                    <div class="row">
                                        <form method="POST" action="./favorite_registration.py">
                                            <input type="hidden" name="restaurant_name" value="{name}">
                                            <input type="hidden" name="access" value="{access}">
                                            <button type="submit"><i class="bi bi-heart"></i></button>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """

if list:
    if not form_address:
        address = "現在地付近のお店"
    else:
        address = form_address + "付近のお店"
else:
    address = "検索結果がありません"

with open('./view/result.html', 'r', encoding='utf-8') as template_file:
    template = template_file.read()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
result = template.format(address=address,tmp=tmp)
print("Content-Type: text/html; charset=utf-8\n")
print(result)
