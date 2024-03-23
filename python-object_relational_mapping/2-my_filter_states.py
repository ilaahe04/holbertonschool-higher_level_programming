#!/usr/bin/python3
"""Connect to database"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}'".format(sys.argv[4])
    cur.execute(query)
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
