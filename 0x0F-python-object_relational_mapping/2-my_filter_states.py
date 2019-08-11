#!/usr/bin/python3

"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    query = """SELECT * FROM states
    WHERE name LIKE '{:s}'
    ORDER BY id ASC""".format(argv[4])

    cur.execute(query)
    allData = cur_sor.fetchall()
    for row in allData:
        print(row)
