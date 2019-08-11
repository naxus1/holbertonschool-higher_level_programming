#!/usr/bin/python3

"""Write a script that takes in an argument and displays all values
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
    cur.execute("SELECT id, name FROM states WHERE BINARY NAME='{}'\
    ORDER BY id ASC".format(argv[4]))

    allData = cur.fetchall()
    for row in allData:
        print(row)
    cur.close()
    db.close()
