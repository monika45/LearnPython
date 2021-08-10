from sqlalchemy import Column, Integer, String, Text
from ScanWord.models.BaseModel import BaseModel


class Item(BaseModel):
    def __init__(self, doc_id):
        super().__init__()
        self.__doc_id = doc_id
        self.table_name = f'items_{doc_id % 100}'
        self.columns = (
            Column('id', Integer, primary_key=True),
            Column('title', String(50), nullable=False),
            Column('content', Text),
            Column('catalogId', Integer, nullable=False),
            Column('documentId', Integer, nullable=False)
        )
