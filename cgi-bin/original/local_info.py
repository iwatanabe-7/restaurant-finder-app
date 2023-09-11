#!/usr/bin/env python3

import requests

cur_location = requests.get("https://get.geojs.io/v1/ip/geo.json").json()
print("緯度:" + cur_location['latitude'])
print("経度:" + cur_location['longitude'])

template = """
<html>
    <head>
        <meta content="text_html; charset=utf-8">
        <title>お店検索</title>
        <link href="//cdn.muicss.com/mui-0.10.3/css/mui.min.css" rel="stylesheet" type="text/css" />
        <script src="//cdn.muicss.com/mui-0.10.3/js/mui.min.js"></script>
    </head>
    <body>
        <h1>できている</h1>
        <div class="mui-container-fluid mui-panel" style="border:7px solid #aaa;">
            <form method="POST" class="mui-form" action="/cgi-bin/original/original_app.py">
                <legend>お店の条件を入力</legend>
                <div class="mui-row mui--text-right">
                    <div class="mui-col-xs-6 mui-col-md-4">
                        <div class="mui-textfield">
                            <input type="text" name="keyword" value="" placeholder="ジャンル">
                        </div>
                    </div>
                </div>
                <div class="mui-row">
                    <div class="mui-col-xs-12 mui-col-md-4">
                        <div class="mui-checkbox">
                            <label><input type="checkbox" name="lunch" value="0" placeholder="0">ランチの有無</label>
                        </div>
                    </div>
                    <div class="mui-col-xs-6 mui-col-md-4">  
                    </div>
                </div>
                <div class="mui-row">
                    <div class="mui-col-xs-6 mui-col-md-4">
                        <div class="mui-textfield">
                            # <input tyoe="text" name="lat" value="{lat}">
                        </div>
                    </div>
                    <div class="mui-col-xs-6 mui-col-md-4">
                        <div class="mui-textfield">
                            # <input tyoe="text" name="lng" value="{lng}">
                        </div>
                    </div>
                </div>
                <button type="submit" class="mui-btn mui-btn--primary "><span class="material-icons">search</span></button>
            </form>
        </div>
        </form>
    </body>
</html>
"""

result = template.format(lat=cur_location['latitude'], lng=cur_location['longitude'])
print("Content-Type: text/html; charset=utf-8\n")
print(result)