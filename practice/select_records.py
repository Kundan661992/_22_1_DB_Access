import psycopg2
from cursor import cursor

try:
    conn = psycopg2.connect(host='localhost',
                            port='5432',
                            user='postgres',
                            password='1234')
    cursor = conn.cursor()
    query = 'select * from vn_student_307'
    cursor.execute(query)
    print("\n retrieving records in db table")
    records = cursor.fetchall
    print("records:", records)
    for each in records:
        print(each)

except Exception as exce:
    print("exception occured ", exce)
finally:
    print("closing and query sent to postgres")
    cursor.close()
    conn.close()
