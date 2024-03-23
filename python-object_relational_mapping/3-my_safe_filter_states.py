#!/usr/bin/python3
"""Connect to database"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY id"
    cur.execute(query)
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
