#!/usr/bin/python

import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sqlite3

conn = sqlite3.connect('data.sqlite')
c = conn.cursor()

app = 'Messenger'

c.execute('''SELECT date, rank FROM leaderboard WHERE name=?
        ORDER BY date ASC''', (app,))

dates = []
ranks = []

for row in c.fetchall():
    dates.append(dt.datetime.strptime(row[0], '%Y-%m-%d').date())
    ranks.append(row[1])

conn.close()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
plt.gca().invert_yaxis()

plt.title('Leaderboard Ranking for ' + app)
plt.xlabel('Date')
plt.ylabel('Rank')

plt.plot(dates, ranks, linestyle='dashed', marker='o')
plt.show()
