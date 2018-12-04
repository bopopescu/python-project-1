# 导入MySQL驱动:
import pymysql

conn = pymysql.connect(host="119.23.240.32", port=3306, user="root" , passwd="ab12345678", db="test",charset="utf8")
cur = conn.cursor()
#cur.execute("create table t_user(id int primary key auto_increment,name varchar(200),age int )");

cur.execute("insert into t_user values(null,'张三',23)");
conn.commit()
cur.execute("select * from t_user");
data = cur.fetchall()
for row in data:
    print(row[0] + row[1] + row[2])
