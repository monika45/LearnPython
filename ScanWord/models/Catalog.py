from sqlalchemy import Table, Column, Integer, String, MetaData, text, update, select
from BaseModel import BaseModel


class Catalog(BaseModel):
    def __init__(self, doc_id):
        super().__init__()
        self.__doc_id = doc_id
        self.__metadata = MetaData()
        self.__table_name = f'catalogs_{doc_id % 50}'
        self.__columns = (
            Column('id', Integer, primary_key=True),
            Column('title', String(200)),
            Column('parentId', Integer),
            Column('documentId', Integer)
        )
