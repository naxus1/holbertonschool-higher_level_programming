#!/usr/bin/python3

"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur_sor = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
    FROM cities JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC"""
    cur_sor.execute(query)
    all_data = cur_sor.fetchall()
    for row in all_data:
        print(row)
