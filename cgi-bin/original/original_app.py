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

# .envファイルの読み込み
load_dotenv()

form = cgi.FieldStorage()
form_address = form.getvalue('address',"")
form_lunch = form.getvalue('lunch',"0")
form_keyword = form.getvalue('keyword',"")
form_lat = form.getvalue('lat',"")
form_lng = form.getvalue('lng',"")
form_shuffle = form.getvalue('shuffle',"")
api_key = (os.environ['API_KEY'])

name = ""
access = ""
address = ""
hp = ""
coupon = ""
tmp=""
template = """"""

# if form_address:
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

# ランダムシャッフル
if form_shuffle:
    random.shuffle(list)

for i, e in enumerate(list):
    name = e.get("name")
    access = e.get("access")
    time = e.get("open")
    close_day = e.get("close")
    hp = e.get("urls").get("pc")
    coupon = e.get("coupon_urls").get("sp")
    img = e.get("photo").get("pc").get("l")
    name = str(name)
    access = html.escape(access)

    tmp += f"""
    <div class="card w-50">
        <div id={i}>
            <p>{name}</p>
            <img src={img} style="width:50%;">
            <p>アクセス：    {access}</p>
            <p>営業時間：    {time}</p>
            <p>休業日：      {close_day}</p>
            <a href="{hp}">ホームページに飛ぶ</a><br>
            <a href="{coupon}">クーポンを見る</a><br>
            <form method="POST" action="./favorite_registration.py">
                <input type="hidden" name="restaurant_name" value="{name}">
                <input type="hidden" name="access" value="{access}">
                <input type="submit" value="お気に入り登録">
            </form>
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
