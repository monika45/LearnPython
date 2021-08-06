from sqlalchemy import create_engine, sql, Table, MetaData


class BaseModel:
    __metadata = MetaData()
    __table_name = ''
    __columns = ()

    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = '33060'
        self.__dbname = 'test'
        self.__username = 'homestead'
        self.__password = 'secret'
        self.__engine = create_engine(
            f'mysql://{self.__username}:{self.__password}@{self.__host}:{self.__port}/{self.__dbname}',
            echo=True)

    def engine(self):
        return self.__engine

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

    def get_table_name(self):
        pass

    def get_metadata(self):
        pass

    def get_columns(self):
        pass

    def get_table(self):
        return Table(self.__table_name, self.__metadata, *self.__columns)

    def create_table(self):
        """
        表不存在时创建表
        """
        self.get_table()
        self.__metadata.create_all(self.__engine)
