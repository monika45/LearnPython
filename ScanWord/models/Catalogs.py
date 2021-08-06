from sqlalchemy import Table, Column, Integer, String, MetaData, text, update, select
from BaseModel import BaseModel


class Catalogs(BaseModel):
    def __init__(self):
        super().__init__()
        self.__metadata = MetaData()

    def __create_table(self, doc_id):
        index = doc_id % 50
        return Table(f'catalogs_{index}', self.__metadata,
                     Column('id', Integer, primary_key=True),
                     Column('title', String(200)),
                     Column('parentId', Integer),
                     Column('documentId', Integer)
                     )

    def get_table(self, doc_id):
        return self.__create_table(doc_id)

    def create_tables(self, doc_ids):
        tables = []
        for docId in doc_ids:
            table = self.__create_table(docId)
            tables = tables + [table]
        self.__metadata.create_all(self.engine())
        return tables


if __name__ == '__main__':
    catalogs = Catalogs()

    # 创建表并插入记录
    # tables = catalogs.create_tables([5, 6])
    # result = catalogs.excute(tables[0].insert().values(title='aaa', documentId=5))
    # print(result.inserted_primary_key)

    # 插入一条记录并获取主键ID
    # table = catalogs.get_table(5)
    # result = catalogs.excute(table.insert().values(title='bb', documentId=5))
    # print(result.inserted_primary_key)

    # 批量插入，列表中数据字典的key必须一致
    # table = catalogs.get_table(5)
    # catalogs.excute(table.insert(), [
    #     {
    #         'title': 'ccc',
    #         'documentId': 5
    #     },
    #     {
    #         'title': 'ddd',
    #         'documentId': 5
    #     }
    # ])

    # 更新，用text从纯文本生成sql
    # table = catalogs.get_table(5)
    # catalogs.excute(table.update().where(text('id=1')).values(title='sss'))

    # 更新,用table.c索引列，删除（delete()）同理
    # table = catalogs.get_table(5)
    # catalogs.excute(table.update().where(table.c.id == 1).values(title='ss2'))

    # 查询所有列
    # table = catalogs.get_table(5)
    # result = catalogs.excute(select(table))
    # # for row in result:
    # #     print(dict(row))
    # # 取一条,指针移动。特殊的key用_mapping取
    # row = result.fetchone()
    # print(row._mapping[table.c.title])

    # 取指定列
    # table = catalogs.get_table(5)
    # result = catalogs.excute(select(table.c.id, table.c.title))
    # row = result.fetchone()
    # print(dict(row))

    # 联表查询


