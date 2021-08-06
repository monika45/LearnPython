from BaseModel import BaseModel
import time
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, text, update, select


class Document(BaseModel):
    __table_name = 'document1'
    __columns = (
        Column('id', Integer, primary_key=True),
        Column('name', String(200)),
        Column('createdAt', TIMESTAMP)
    )

    def get_table_name(self):
        return self.__table_name

    def get_metadata(self):
        return self.__metadata

    def get_columns(self):
        return self.__columns


if __name__ == '__main__':
    doc = Document()
    doc.create_table()

    # res = doc.excute('select "hello world"')
    # print(res)
    # doc.excute(f'insert into document(name,createdAt) values ("a", "{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")')
    # datas = [
    #     {
    #         'name': 'a',
    #         'createdAt': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     },
    #     {
    #         'name': 'b',
    #         'createdAt': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     },
    #     {
    #         'name': 'c',
    #         'createdAt': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     }
    # ]

    # print(",".join([str(item) for item in [tuple(data.values()) for data in datas]]))

    # doc.excute('truncate table document')
    # res = doc.insert('document', datas)
    # res = doc.excute('select id, name from document')
    # for row in res:
    #     print(row.name)

    # print()

    # print(res)
