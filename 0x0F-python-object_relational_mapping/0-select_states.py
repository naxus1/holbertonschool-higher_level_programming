#!/usr/bin/env python3
"""script that lists all states from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur_sor = db.cursor()
    cur_sor.execute("SELECT * FROM states ORDER BY id ASC")
    all_data = cur_sor.fetchall()
    for row in all_data:
        print(row)
