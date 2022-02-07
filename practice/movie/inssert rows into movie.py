import psycopg2
from cursor import cursor

try:
    conn = psycopg2.connect(host='localhost',
                            port='5432',
                            user='postgres',
                            password='1234')
    cursor = conn.cursor()
    rec1 = "insert into movie values('26sep2021', 'paagal', 2)"
    rec2 = "insert into movie values('26sep2021', 'saaho', 5)"
    rec3 = "insert into movie values('26sep2021', 'love', 9)"
    rec4 = "insert into movie values('27sep2021', 'Bahubali', 11)"
    rec5 = "insert into movie values('27sep2021', 'Bahubali2', 2)"

    cursor.execute(rec1)
    cursor.execute(rec2)
    cursor.execute(rec3)
    cursor.execute(rec4)
    cursor.execute(rec5)
    conn.commit()
except Exception as exce:
    print("Exception occurred:", exce)
finally:
    print("cursor and connection closed data sent to db")
    cursor.close()
    conn.close()