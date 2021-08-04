from BaseModel import BaseModel
import time


class Document(BaseModel):
    pass


if __name__ == '__main__':
    doc = Document()
    # res = doc.query('select "hello world"')
    # print(res)
    # doc.excute(f'insert into document(name,createdAt) values ("a", "{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")')
    datas = [
        {
            'name': 'a',
            'createdAt': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        },
        {
            'name': 'b',
            'createdAt': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        },
        {
            'name': 'c',
            'createdAt': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
    ]

    # print(",".join([str(item) for item in [tuple(data.values()) for data in datas]]))

    # doc.excute('truncate table document')
    # res = doc.insert('document', datas)
    # res = doc.query('select id, name from document')
    # for row in res:
    #     print(row.name)


    # print()


    # print(res)


