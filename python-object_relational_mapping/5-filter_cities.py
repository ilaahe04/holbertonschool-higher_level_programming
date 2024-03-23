#!/usr/bin/python3
"""
Script to list all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py mysql_username mysql_password database_name state_name")
        sys.exit(1)
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        query = "SELECT * FROM cities WHERE state_name = %s ORDER BY id"
        cur.execute(query, (sys.argv[4],))
        cities = cur.fetchall()
        for city in cities:
            print(city)
        cur.close()
        db.close()
