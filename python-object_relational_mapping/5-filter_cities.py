#!/usr/bin/python3
"""
Script to list all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys
import sqlalchemy

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id")
    print(", ".join([c[2] for c in cur.fetchall() if c[4] == sys.argv[4]]))
