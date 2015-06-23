Market Leaderboard Tracker
==========================

Utilities to track the list of top apps on Google Play. Data is stored in a SQLite database and output in graph form via Matplotlib.

Requirements
------------

* Python 3
* lxml
* requests
* matplotlib

Linux users: If charts are not being generated, try using the Matplotlib package from your distribution's repositories if available instead of installing via `pip`.

Scripts
-------

### fetch.py

Retrieves the list of top apps and stores it in a SQLite database. This script should be run at regular intervals (e.g. cron tabs for daily or weekly) to create useful data.

The default category is the "top-selling (free)", and individual categories are not yet accounted for.

The number of retrieved apps is whatever Google Play would show a user without them having to scroll down, which is currently 60.

### historic.py

Creates a line plot of a specific app's performance on the app leaderboard over the course of the data collection period.

The default app to track is Messenger.

### top.py

Creates a bar graph of apps that have reached position #1 during the data collection period against the number of occurrences per app.

Web interface
-------------

TODO
