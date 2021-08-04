from sqlalchemy import Table, Column, Integer, String, MetaData
from BaseModel import BaseModel

class Catalogs(BaseModel):
    def createTable(self):
        metadata = MetaData()
        catalogs_1 = Table('catalogs_1', metadata,
            Column('id', Integer, primary_key=True),
            Column('title', String),
            Column('parentId', Integer),
            Column('documentId', Integer)
        )
        catalogs_2 = Table('catalogs_2', metadata,
            Column('id', Integer, primary_key=True),
            Column('title', String),
            Column('parentId', Integer),
            Column('documentId', Integer)
        )


