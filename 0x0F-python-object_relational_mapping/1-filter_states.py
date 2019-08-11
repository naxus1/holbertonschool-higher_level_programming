#!/usr/bin/python3
"""cript that lists all states with a name starting with N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur_sor = db.cursor()
    cur_sor.execute("""SELECT * FROM states
    WHERE name LIKE BINARY 'N%'
    ORDER BY id ASC""")
    all_data = cur_sor.fetchall()
    for row in all_data:
        print(row)
