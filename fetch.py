#!/usr/bin/python

from lxml import html

import re
import requests

page = requests.get('https://play.google.com/store/apps/collection/topselling_free')
tree = html.fromstring(page.text)

# Create a list of apps
apps = tree.xpath('//h2/a[@class="title"]/text()')

# Trim lines and remove blank lines
apps = [line.strip() for line in apps]
apps = filter(None, apps)

for app in apps:
    # Remove numeric rank identifier portion
    app = re.sub('^[0-9]*\.\ *', '', app)
    print (app)
