from pymysql import Connection
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='1234'
)
cursor = conn.cursor()
conn.select_db("epas")
# cursor.execute("CREATE TABLE test_mysql(id INT, info VARCHAR(255))")
cursor.execute("select * from t_member")
data: tuple = cursor.fetchall()
for i in data:
    print(i)
print(conn.get_server_info())
conn.close()
