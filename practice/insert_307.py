import psycopg2
from cursor import cursor

try:
    conn = psycopg2.connect(host='localhost',
                            port='5432',
                            user='postgres',
                            password='1234')
    cursor = conn.cursor()

    rec1 = "INSERT INTO VN_STUDENT_307 VALUES(104, 'johnabrahm', 'anantapur')"
    rec2 = "insert into VN_STUDENT_307 values(105, 'shyamkunda', 'anantapur')"
    rec3 = "insert into VN_STUDENT_307 values(106, 'krishna', 'anantapur')"
    cursor.execute(rec1)
    cursor.execute(rec2)
    res = cursor.execute(rec3)

    conn.commit()

except Exception as exce:
    print("Exception occured", exce)

finally:
    print("closing cursor and connection")
    cursor.close()
    conn.close()




