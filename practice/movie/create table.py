import psycopg2
from cursor import cursor

try:
    conn = psycopg2.connect(host='localhost',
                            port='5432',
                            user='postgres',
                            password='1234')
    cursor = conn.cursor()
    query = "CREATE TABLE MOVIE(DATE VARCHAR(25), NAME VARCHAR(25), SHOWTIME INTEGER)"
    cursor.execute(query)
    conn.commit()
except Exception as exce:
    print("Exception occurred: ", exce)
finally:
    print("closing cursor and connection and data sent to postgres")
    cursor.close()
    conn.close()



