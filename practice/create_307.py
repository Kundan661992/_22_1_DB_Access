import psycopg2
from cursor import cursor
# step 1 get connection
# step 2 get cursor
# step 3 prepare query
# step 4 execute query
# step 5 commit query

try:
    # 1 get connection
    conn = psycopg2.connect(host='localhost',
                            port='5432',
                            user='postgres',
                            password='1234')
    print("Type of connection:", type(conn), conn)
    # get cursor on db connection
    cursor = conn.cursor()
    print("Type of cursor:", type(cursor), cursor)
    # 3. prepare query
    query = "CREATE TABLE VN_STUDENT_307(id INTEGER, name VARCHAR(25), location VARCHAR(25))"
    # 4. execute query
    cursor.execute(query)
    # 5. commit query
    conn.commit()

except Exception as exce:
    print("Exception occured", exce)

finally:
    print("closing cursor and connection")
    cursor.close()
    conn.close()


