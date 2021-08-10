from sqlalchemy import create_engine, sql, Table, MetaData
import time


class BaseModel:
    table_name = ''
    columns = ()
    metadata = None

    # 时间字段
    created_at = None
    updated_at = None

    table = None

    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = '33060'
        self.__dbname = 'test'
        self.__username = 'homestead'
        self.__password = 'secret'
        self.__engine = create_engine(
            f'mysql://{self.__username}:{self.__password}@{self.__host}:{self.__port}/{self.__dbname}',
            echo=True)

        self.metadata = MetaData()

    def engine(self):
        return self.__engine

    def conn(self):
        return self.engine().connect()

    def insert(self, table, data_list):
        """
        table: 表名
        data_list: 字典列表
        """
        if len(data_list) == 0:
            return False
        fields = [key for key in data_list[0]]
        with self.__engine.connect() as conn:
            conn.execute(sql.expression.text(f"INSERT INTO {table} ({','.join(fields)}) VALUES "
                                             f"({','.join([':' + key for key in fields])})"),
                         data_list)
        return True

    def excute(self, sql, datas=None):
        with self.__engine.connect() as conn:
            if datas:
                return conn.execute(sql, datas)
            return conn.execute(sql)

    def get_table(self):
        if self.table is None:
            self.table = Table(self.table_name, self.metadata, *self.columns)
        return self.table

    def has_table(self, table_name=None):
        """
        表是否存在
        """
        if table_name is None:
            table_name = self.table_name
        return self.engine().has_table(sql.quoted_name(table_name, True))

    def create_table(self):
        """
        表不存在时创建表
        """
        if self.has_table():
            return True
        self.get_table()
        self.metadata.create_all(self.__engine)
        return True

    def complete_time_fields(self, data):
        """
        填充时间字段值
        data: 数据字典
        """
        if self.created_at and self.created_at not in data.keys():
            data[self.created_at] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        if self.updated_at and self.updated_at not in data.keys():
            data[self.updated_at] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        return data

    def insert_all(self, datas):
        """
        批量插入，自动填充时间字段
        datas: 数据字典列表
        """
        datas = [self.complete_time_fields(data) for data in datas]
        self.excute(self.get_table().insert().values(datas))
        return True

    def insert_get_id(self, data):
        """
        插入一条记录并获取主键值。
        自动插入时间字段
        data: 字典
        """
        data = self.complete_time_fields(data)
        result = self.excute(self.get_table().insert().values(data))
        return result.inserted_primary_key

    def update(self, where, data):
        if self.updated_at and self.updated_at not in data.keys():
            data[self.updated_at] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        result = self.excute(self.get_table().update().where(where).values(data))
        return result
