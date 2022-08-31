import MySQLdb
import sys
if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost",
                        port=3306,
                        user=sys.argv[0],
                        passwd=sys.argv[1],
                        db=sys.argv[2])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
