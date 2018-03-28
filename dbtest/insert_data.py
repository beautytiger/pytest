from sqlalchemy.engine import create_engine
import random
from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        before = time()
        result = func(*args, **kwargs)
        after = time()
        print(after-before)
        return result
    return wrapper


class MYSQLConn(object):
    _conn = "mysql+mysqldb://{user}:{pwd}@{host}:{port}/{db}?charset={charset}"

    def __init__(self, host="localhost",
                 port=3306,
                 user="root",
                 passwd="root",
                 database="specialdb",
                 charset='utf8mb4',
                 ):
        self._full_conn = self._conn.format(
            user=user,
            pwd=passwd,
            host=host,
            port=port,
            db=database,
            charset=charset,
        )
        self.max = 18446744073709551615  # unsigned bigint type
        self._engine = create_engine(self._full_conn, pool_recycle=30)

    @timer
    def insert_num(self, rows=10**3):
        """插入数据，每次一行"""
        sql = """
            insert into indexed_num
            (col_value)
            values
            (%s)
        """
        for i in range(rows):
            value = random.randint(0, self.max)
            self._engine.execute(sql, (value, ))

    @timer
    def insert_num2(self, rows=10**3//2):
        """插入数据，每次两行"""
        sql = """
            insert into indexed_num
            (col_value)
            values
            (%s),
            (%s)
        """
        for i in range(rows):
            value1 = random.randint(0, self.max)
            value2 = random.randint(0, self.max)
            self._engine.execute(sql, (value1, value2))

    @timer
    def insert_numn(self, row_per_query=1000, total_query=1000):
        """插入数据，每次row_per_query行, 共插入total_query次"""
        sql_a = """
            insert into indexed_num
            (col_value)
            values
        """
        sql_b = """
            (%s),
        """

        sql_e = """
            (%s)
        """
        sql = sql_a
        for i in range(row_per_query-1):
            sql += sql_b
        sql += sql_e

        for i in range(total_query):
            value = list()
            for j in range(row_per_query):
                value.append(random.randint(0, self.max))
            self._engine.execute(sql, value)


if __name__ == '__main__':
    conn = MYSQLConn()
    # conn.insert_num()  # about 100 queries per second
    # conn.insert_num2()  # about 100 queries per second
    conn.insert_numn(1000, 1000)  # takes 14~17 second
    conn.insert_numn(10000, 100)  # takes 12~24 second, time increase as row increase in database


