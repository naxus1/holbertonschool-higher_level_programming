#!/usr/bin/python3

"""
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
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
    cur_sor.execute(""" SELECT cities.name
    FROM cities JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE %s
    ORDER BY states.name """, (argv[4],))
    all_data = cur_sor.fetchall()
    len_data = len(all_data)

    for i in range(len_data):
        if i < len_data - 1:
            print("{}, ".format(all_data[i][0]), end="")
        else:
             print("{}".format(all_data[i][0]))

    cur_sor.close()
    db.close()
