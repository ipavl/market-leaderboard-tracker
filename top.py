#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import sqlite3

conn = sqlite3.connect('data.sqlite')
c = conn.cursor()

c.execute('''SELECT name, COUNT(*) FROM leaderboard
        WHERE rank=1 GROUP BY name, rank''')

names = []
count = []

for row in c.fetchall():
    names.append(row[0])
    count.append(row[1])

x = np.arange(len(names))

plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

plt.title('Top of Leaderboard Records')
plt.xlabel('App')
plt.ylabel('Occurrences')

plt.bar(x, count, align='center')
plt.xticks(x, names)

plt.show()
