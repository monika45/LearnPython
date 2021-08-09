import sys

from sqlalchemy import Table, Column, Integer, String, MetaData, text, update, select
from ScanWord.models.BaseModel import BaseModel


class Catalog(BaseModel):

    def __init__(self, doc_id):
        super().__init__()
        self.__doc_id = doc_id
        self.table_name = f'catalogs_{doc_id % 50}'
        self.columns = (
            Column('id', Integer, primary_key=True),
            Column('title', String(200), nullable=False),
            Column('parentId', Integer, default=0),
            Column('documentId', Integer, nullable=False)
        )
