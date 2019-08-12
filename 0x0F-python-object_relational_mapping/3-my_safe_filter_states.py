#!/usr/bin/python3
"""script SQL inyection that takes in arguments
"""


if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name = %s", (argv[4],))
    allData = cur.fetchall()
    for row in allData:
        print(row)
    cur.close()
    bd.close()
