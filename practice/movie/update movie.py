import psycopg2
from cursor import cursor

try:
    conn = psycopg2.connect(host='localhost',
                            port='5432',
                            user='postgres',
                            password='1234')
    cursor = conn.cursor()
    query = "update movie set name = 'lion' where showtime = 2 and name = 'paagal'"

    cursor.execute(query)
    conn.commit()
except Exception as exce:
    print("Exception occurred: ", exce)
finally:
    print("cursor and connection are closed and dat sent to db")
    cursor.close()
    conn.close()


import psycopg2
from cursor import cursor

try:
    conn = psycopg2.connect(host='localhost',
                            port='5432',
                            user='postgres',
                            password='1234')
    cursor = conn.cursor()
    query = "update movie set name = 'hello' where name = 'lion' and date = '27sep2021'"
    cursor.execute(query)
    conn.commit()
except Exception as exce:
    print("Exception occurred:", exce)
finally:
    print("cursor and connection are closed and request sent to db")
    cursor.close()
    conn.close()



