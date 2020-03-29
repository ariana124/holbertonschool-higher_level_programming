#!/usr/bin/python3
"""
Contains a script that filters state names based on user input from
the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user = argv[1]
    passwd = argv[2]
    database = argv[3]
    sname = argv[4]

    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=passwd, db=database)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (sname, ))

    rows = cur.fetchall()
    for state in rows:
        print(state)

    cur.close()
    db.close()
