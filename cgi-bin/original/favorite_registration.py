#!/usr/bin/env python3

import sqlite3
import requests
import json
import cgi
import html
import logging
import sys
import io

connection = sqlite3.connect("company.sqlite3")
cur = connection.cursor()
tmp = ""

try:
    cur.execute("create table if not exists company(name text, access text);")
except sqlite3.OperationalError:
    cur.execute("delete from company")

form = cgi.FieldStorage()
form_name = form.getvalue('restaurant_name', "")
form_access = form.getvalue('access', "")

cur.execute('insert into company values (?, ?)', (form_name, form_access))
cur.execute('select * from company')
data = cur.fetchall()

for i, row in enumerate(data):
    name = html.escape(row[0])
    access = html.escape(row[1])

    tmp += f"""
        <div class="mui-col-xs-3 mui-col-md-3" id={i}>
            <p>{name}</p>
            <p>{access}</p>
        </div>
    """

connection.commit()

template = """
<html>
    <head>
        <meta content="text/html; charset=utf-8">
        <title>お気に入り登録完了</title>
        <link href="//cdn.muicss.com/mui-0.10.3/css/mui.min.css" rel="stylesheet" type="text/css" />
        <script src="//cdn.muicss.com/mui-0.10.3/js/mui.min.js"></script>
        
    </head>
    <body>
        <h1>登録完了</h1>
        <a href="../../original/original.html">検索を続ける</a> 
        <h2>登録したお店の一覧</h2>
        {tmp} 
    </body>
</html>
"""

result = template.format(tmp=tmp)

print("Content-Type: text/html;charset=utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
sys.stdout.buffer.write(result.encode('utf-8'))
