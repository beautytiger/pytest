import MySQLdb


db = MySQLdb.connect(
    host='localhost',
    user='wxmall',
    passwd='wxmall',
    db='sm',
    charset='utf8mb4',
)

db.autocommit(on=True)

cur = db.cursor()

cur.execute("select * from weixin_wechatsubscribeuser limit 1;")

# print('testing fetchall()')
# for row in cur.fetchall():
#     print(row[0], " ", row[1])
print('testing fetchone...')
data = cur.fetchone()
print(data)

print('show mysql verison...')
cur.execute("select version();")
print(cur.fetchone())

print('drop table...')
cur.execute('drop table if exists `employee`')

print('create_table')
create_table = """create table employee (
    first_name varchar(63) not null,
    last_name varchar(63),
    age int,
    sex varchar(1),
    income float)"""

cur.execute(create_table)

print('insert data...')
insert_data = """insert into 
    `employee`(first_name, last_name, age, sex, income)
    values ('Mac', 'Mohan', 20, 'M', 2000);"""

try:
    cur.execute(insert_data)
    # db.commit()
except Exception as e:
    print(e)
    # db.rollback()

print("show columns...")
show_column = """desc employee;"""
cur.execute(show_column)
for col in cur.fetchall():
    print(col)

print('another way...')
cur.execute('show columns from employee;')
print(cur.fetchall())

print('query...')
query_data = """select * from employee;"""

cur.execute(query_data)
for row in cur.fetchall():
    print(row)

cur.close()
db.close()
