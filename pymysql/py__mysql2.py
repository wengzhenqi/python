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
insert_dep1 = 'insert into departments VALUES (%s, %s)'     #变量
#########################添加字段##########################
# deps = [(1, '人事部'),(2, '运维部'),(3, '开发部'),(4, '市场部')]
# cursor.executemany(insert_dep1,deps)
###########################################################
# dep1 = [(5, '测试部')]
# cursor.executemany(insert_dep1, dep1)
############################################################
# dep2 = [(6, '财务部'), (7, '运营部')]
# cursor.executemany(insert_dep1,dep2)
##########################修改字段名#############################
# update_hr = 'update departments set dep_name=%s where dep_name=%s'
# data = ('人力资源部', '人事部')                 #修改字段名 注意execute
# cursor.execute(update_hr,data)
##########################删除操作#################################
# del_yy = 'delete from departments where dep_name = %s'
# yy_dep = ('运营部')
# cursor.execute(del_yy,yy_dep)           #删除操作



##########################查询操作################################
# select1 = 'select * from departments ORDER by dep_id'
# cursor.execute(select1)
# result = cursor.fetchone()          #取一行记录
# print(result)
# result2 = cursor.fetchall()           #取全部记录
# print(result2)
result3 = cursor.fetchmany(2)           #取两行
print(result3)
#################################################################
# select2 = 'select * from departments ORDER by dep_id'
# cursor.execute(select2)
# cursor.scroll(3, mode='absolute')       #以绝对方式向下移动3条记录
# result1 = cursor.fetchone()
# cursor.scroll(-1)         #默认以相对方式移动
# result2 = cursor.fetchone()
# print(result1)
# print('#' * 30)
# print(result2)

conn.commit()       #提交改动
cursor.close()      #关闭游标
conn.close()        #关闭连接