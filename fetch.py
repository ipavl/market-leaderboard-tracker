#!/usr/bin/python

from lxml import html

import re
import requests
import sqlite3
import time

page = requests.get('https://play.google.com/store/apps/collection/topselling_free')
tree = html.fromstring(page.text)

# Create a list of apps
apps = tree.xpath('//h2/a[@class="title"]/text()')
apps_ids = tree.xpath('//h2/a[@class="title"]/@href')

# Trim lines and remove blank lines
apps = [line.strip() for line in apps]
apps = filter(None, apps)

# Database setup
conn = sqlite3.connect('data.sqlite')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS leaderboard
        (name TEXT, appid TEXT, date TEXT, rank INTEGER)''')

data = []
date = time.strftime('%Y-%m-%d')

for i, app in enumerate(apps):
    # Remove numeric rank identifier portion
    app = re.sub('^[0-9]*\.\ *', '', app)

    # Get the app ID from href
    pkg = apps_ids[i].split('=')[1]

    data.append((app, pkg, date, i + 1))

# Store the data in the database
c.executemany('INSERT INTO leaderboard VALUES (?, ?, ?, ?)', data)

conn.commit()
conn.close()
