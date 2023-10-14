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

cur.execute('select * from company')
data = cur.fetchall()

for i, row in enumerate(data):
    name = html.escape(row[0])
    access = html.escape(row[1])

    tmp += f"""
        <div class="company_info" id="{i + 1}">
            <p>{name}</p>
            <p>{access}</p>
        </div>
        <br>
    """

connection.commit()

template = f"""
    <html>
        <head>
            <meta content="text/html; charset=utf-8">
            <title>お気に入り登録完了</title>
        </head>
        <body>
            <h2>登録したお店の一覧</h2>
                {tmp}
            <a href="../../view/original.html">検索</a> 
        </body>
    </html>
"""

result = template.format(tmp=tmp)

print("Content-Type: text/html;charset=utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
sys.stdout.buffer.write(result.encode('utf-8'))
