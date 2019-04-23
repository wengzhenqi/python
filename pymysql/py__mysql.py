import pymysql

#创建数据库的连接
conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123qqq...A',
    db = 'nsd1811',
    charset = 'utf8'
)

cursor = conn.cursor()      #创建游标
#SQL语句
# create_dep = 'create table departments(dep_id int,dep_name VARCHAR(20),PRIMARY KEY(dep_id) )'
# cursor.execute(create_dep)        #执行sql语句
###################################
# create_emps = 'create table employees(emp_id int,emp_name VARCHAR(20),email VARCHAR(50),dep_id int,PRIMARY key(emp_id),FOREIGN key(dep_id) REFERENCES departments(dep_id))'
# cursor.execute(create_emps)
###################################
create_sal = 'create table salary(auto_id int,emp_id int,date DATE ,basic int,awards int,PRIMARY KEY(auto_id), FOREIGN KEY(emp_id) REFERENCES employees(emp_id))'
cursor.execute(create_sal)
conn.commit()       #提交改动
cursor.close()      #关闭游标
conn.close()        #关闭连接