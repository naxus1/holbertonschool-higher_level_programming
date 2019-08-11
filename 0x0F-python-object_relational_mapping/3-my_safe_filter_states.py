#!/usr/bin/python3
"""
safe from MySQL injections
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    access = db.cursor()
    access.execute("SELECT * FROM states WHERE states.name = %s", (argv[4],))
    rows = access.fetchall()
    for row in rows:
        print(row)
