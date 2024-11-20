"""
blocklist.py

This file contains the blocklist of the JWT tokens. It will be imported by
app and the logout resource so that tokens can be added to the blocklist
when the user logs out.

Probably would want to use a DB for the blocklist as opposed to a Python
set. This is because if the app is restarted then the blocklist will be
erased, so previously expired tokens would be able to make requests.
Python sets do not persist
"""

BLOCKLIST = set()