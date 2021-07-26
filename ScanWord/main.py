import docx

file = docx.Document('中华人民共和国民法典2020.docx')

paraLen = len(file.paragraphs)
print('段落数：' + str(paraLen))

# for paraIndex in range(paraLen):
#     para = file.paragraphs[paraIndex]
#     if para.text != '':
#         print('段：' + str(paraIndex))
#         print(para.text)
#     for run in para.runs:
        # print(run.text)
        # print(run.font.name)


for para in file.paragraphs:
    if para.text != '':
        print(para.text)
