#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
"""
import MySQLdb
import sys
if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN\
        states ON states.name= %s AND\
            cities.state_id=states.id;", (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join([state[0] for state in query_rows]))
    cur.close()
    conn.close()
