import xlrd
import xlwt
import random

headers = ['姓名', '语文', '数学', '英语']
first_names = '赵钱孙李王陆曾吴印余俞于曹刘甄林贾丁陈朱张贺彭尹何罗'
last_names = '玉鱼雨闻文果清青期数床前明月光三期大非九天魅族得无玫瑰麦克'
filename = '../res/成绩表.xls'


def create_name():
    """随机生成姓名"""
    return random.choice(first_names) + ''.join(random.sample(last_names, 2))


def write_excel():
    """写入excel"""
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1')
    for index, head in enumerate(headers):
        sheet1.write(0, index, head)
    for row in range(1, 21):
        sheet1.write(row, 0, create_name())
    for row in range(1, 21):
        for col in range(1, 4):
            sheet1.write(row, col, random.randint(1, 100))
    workbook.save(filename)


def read_excel():
    """读取excel"""
    workbook = xlrd.open_workbook(filename)
    sheet1 = workbook.sheet_by_index(0)
    # 总行数和列数
    # print(sheet1.nrows, sheet1.ncols)
    students = []
    title = [col.value for col in sheet1.row(0)]
    for i in range(1, sheet1.nrows):
        row_values = sheet1.row_values(i, 0, sheet1.ncols)
        students.append(dict(zip(title, row_values)))
    print(students)


def edit_excel():
    """编辑excel"""
    rwb = xlrd.open_workbook(filename)
    sheet1 = rwb.sheet_by_index(0)
    sheet1.put_cell(0, 4, xlrd.XL_CELL_TEXT, '总分', None)
    # print(sheet1.row_values(0))
    # 算总分
    nrows = sheet1.nrows
    for rowx in range(1, nrows):
        total_score = sum(sheet1.row_values(rowx, 1, 4))
        sheet1.put_cell(rowx, 4, xlrd.XL_CELL_NUMBER, round(total_score), None)
    # 算平均分
    for colx in range(1, 5):
        avg = sum(sheet1.col_values(colx, 1, nrows)) / (nrows - 1)
        sheet1.put_cell(nrows, colx, xlrd.XL_CELL_NUMBER, round(avg), None)
    # 保存编辑后的表格
    wwb = xlwt.Workbook()
    sheetw = wwb.add_sheet('sheet1')
    nrows = sheet1.nrows
    ncols = sheet1.ncols
    for row in range(0, nrows):
        for col in range(0, ncols):
            sheetw.write(row, col, sheet1.cell_value(row, col))
    wwb.save(filename)


if __name__ == '__main__':
    edit_excel()
