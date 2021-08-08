import sys

from sqlalchemy import Table, Column, Integer, String, MetaData, text, update, select
from ScanWord.models.BaseModel import BaseModel


class Catalog(BaseModel):
    columns = (
        Column('id', Integer, primary_key=True),
        Column('title', String(200)),
        Column('parentId', Integer),
        Column('documentId', Integer)
    )

    def __init__(self, doc_id):
        super().__init__()
        self.__doc_id = doc_id
        self.table_name = f'catalogs_{doc_id % 50}'
