from sqlalchemy import create_engine,sql


class BaseModel:
    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = '33060'
        self.__dbname = 'test'
        self.__username = 'homestead'
        self.__password = 'secret'
        self.__engine = create_engine(f'mysql://{self.__username}:{self.__password}@{self.__host}:{self.__port}/{self.__dbname}',
                                    echo=True)

    def query(self, sql_str):
        with self.__engine.connect() as conn:
            result = conn.execute(sql_str)
            return result

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

    def excute(self, sql):
        with self.__engine.connect() as conn:
            conn.execute(sql)






