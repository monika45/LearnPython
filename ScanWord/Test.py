import sys
import time
from sqlalchemy import text, select, case, func, distinct, sql
from ScanWord.models.Catalog import Catalog
from Scan
Word.models.Document import Document

if __name__ == '__main__':
    # 创建表、批量插入记录、插入记录并获取主键ID、更新记录、查询
    # document = Document()
    # document.create_table()
    # id = document.insert_get_id({
    #     'name': 'aaa'
    # })
    # print(id)
    # id = document.insert_get_id({
    #     'name': 'bbb'
    # })
    # print(id)
    # id = document.insert_get_id({
    #     'name': 'ccc'
    # })
    # print(id)
    # document.update(text('id=1'), {
    #     'name': 'sss'
    # })
    #
    # catalog1 = Catalog(1)
    # catalog1.create_table()
    # catalog1.insert_all([
    #     {
    #         'title': '1.aaa',
    #         'documentId': 1
    #     },
    #     {
    #         'title': '2.bbb',
    #         'documentId': 1
    #     }
    # ])
    # catalog2 = Catalog(2)
    # catalog2.create_table()
    # catalog2.insert_all([
    #     {
    #         'title': '1.ccc',
    #         'documentId': 2
    #     },
    #     {
    #         'title': '2.ddd',
    #         'documentId': 2
    #     }
    # ])
    #
    # print(document.excute(select(document.get_table())).all())
    # print(catalog1.excute(select(catalog1.get_table())).all())
    # print(catalog2.excute(select(catalog2.get_table())).all())

    # 联表查询
    # document = Document()
    # t_doc = document.get_table()
    # catlog1 = Catalog(1)
    # t_catalog1 = catlog1.get_table()
    # s = select(t_doc, t_catalog1).where(t_doc.c.id == t_catalog1.c.documentId)
    # for row in document.excute(s):
    #     print(dict(row))

    # 字符串形式
    # print(str(t_doc.c.id == t_catalog1.c.documentId))


    # 运算符
    # document = Document()
    # t_doc = document.get_table()
    # print(t_doc.c.id == 7) # document.id = :id_1
    # print((t_doc.c.id == 7).compile().params) #{'id_1': 7}
    # print(t_doc.c.id != 7) #document.id != :id_1
    # print(t_doc.c.name == None) #document.name IS NULL

    # t_doc.c.name.op('任何操作符')(第二个参数)
    # t_doc.c.name.like('%a%')
    # t_doc.c.name.ilike('%a%')


    # case...when...then...end
    # document = Document()
    # doc_t = document.get_table()
    # stmt = select(doc_t).\
    #     where(
    #         case(
    #             (doc_t.c.name == 'sss', doc_t.c.id > 0),
    #             (doc_t.c.name == 'bbb', 'B'),
    #             else_='A'
    #         )
    #     )
    # print(document.excute(stmt).all())

    # func和distinct
    # document = Document()
    # doc_t = document.get_table()
    # stmt = select(func.count(doc_t.c.name))
    # print(document.excute(stmt).all())
    # print(document.excute(select(distinct(doc_t.c.name))).all())


    # 表是否存在
    # document = Document()
    # print(document.has_table('catalogs_4'))

