#!/usr/bin/python3

"""
write a script that takes in arguments and displays all values
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur = execute("SELECT * FROM states WHERE states.name = %s", (argv[4],))
    allData = cur.fetchall()
    for row in allData:
        print(row)
    cur.close()
    conn.close()
