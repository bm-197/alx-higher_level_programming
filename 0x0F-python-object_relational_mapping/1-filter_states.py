#!/usr/bin/python3
"""
Script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(usr=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FORM states ORDER BY id")
    states = c.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
