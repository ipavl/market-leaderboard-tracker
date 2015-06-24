#!/usr/bin/python

from bottle import route, run

import json
import sqlite3

conn = sqlite3.connect('data.sqlite')
c = conn.cursor()

'''
Returns how many times each app has achieved rank 1.
'''
@route('/top', method='GET')
def leaderboard_top():
    c.execute('''SELECT appid, COUNT(*) FROM leaderboard
            WHERE rank=1 GROUP BY appid, rank''')

    return json.dumps(dict(c.fetchall()))

'''
Returns an app's leaderboard performance over time.
'''
@route('/app/<id>', method='GET')
def app_lookup(id):
    c.execute('''SELECT date, rank FROM leaderboard
            WHERE appid=? ORDER BY date ASC''', (id,))

    return json.dumps(dict(c.fetchall()))

try:
    run(port=8080)

finally:
    conn.close()
