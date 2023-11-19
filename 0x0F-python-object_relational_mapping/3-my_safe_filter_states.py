#!/usr/bin/python3
"""
Script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument. But this time, write one
that is safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
        FROM `states`\
            WHERE BINARY `name` = %s", (sys.argv[4], ))
    rows = c.fetchall()
    [print(row) for row in rows]