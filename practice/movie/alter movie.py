import psycopg2
from cursor import cursor


try:
    conn = psycopg2.connect(host='localhost',
                            port='5432',
                            user='postgres',
                            password='1234')
    cursor = conn.cursor()
    query = "alter table movie add column price integer"
    cursor.execute(query)
    conn.commit()

except Exception as exce:
    print("Excepion occured as ", exce)

finally:
    print("cursor and connections are closed")
    cursor.close()
    conn.close()

