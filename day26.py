from pymysql import Connection
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='1234'
)
cursor = conn.cursor()
conn.select_db("epas")
cursor.execute("insert into test_mysql values (1, 123)")
conn.commit()
conn.close()
