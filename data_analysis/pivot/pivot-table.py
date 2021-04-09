import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def pivot():
    """
    数据透视
    :return:
    """
    p_data = pd.read_excel('test2.xlsx', sheet_name='Sales Report', header=2)
    col = p_data.columns.values
    pt = pd.pivot_table(p_data, index=['Product ', 'Loading Date ', 'Logistics Status '], columns=[], values=[
        'Loading Weight ',
        'Container No. '
    ], aggfunc={
        'Loading Weight ': np.sum,
        'Container No. ': 'count'
    }, margins=True, fill_value=0)
    # 筛选功能
    # 列表可以传多个参数
    pt = pt.query('`Logistics Status `== ["Finished", "Ready For Sending Waybill", "Waiting For Bol from Forwarders"]')
    pt = pt.query('"2021-01-01" < `Loading Date ` < "2021-01-31"')
    pt.to_excel('pt.xlsx')

    # 指定表单名，不导出index指定的列
    # pt.to_excel('pt1.xlsx', sheet_name='Jan-21', index=False)


def subset():
    """
    读写表格、过滤、选择子集、修改数据
    :return:
    """
    # usecols指定使用哪些列
    # dataframe
    # df = pd.read_excel('test2.xlsx', sheet_name='Sales Report', header=2, usecols='A:CA')
    # 前3行
    # print(df.head(3))
    # 后3行
    # print(df.tail(3))
    # 查看表格信息
    # print(df.info())

    # 取一列
    # products = df['Product ']
    # 每个列都是一个Series，可以用type()验证
    # print(type(products))
    # print(products.shape)

    # 取两列
    # two_colums = df[['Product ', 'Load Number ']]
    # print(two_colums.head(3))
    # 返回结果是DataFrame
    # print(type(two_colums))
    # print(two_colums.shape)

    # 过滤 df[表达式，> < == 等]  df.loc/iloc[行选择，列选择]
    # filteredByStatusDf = df[df['Logistics Status '] == "Finished"]
    # print(filteredByStatusDf)
    # in
    # filteredInStatusDf = df[df['Logistics Status '].isin(['Finished', 'Ready For Sending Waybill', 'Waiting For Bol from Forwarders'])]
    # print(filteredInStatusDf)
    # | &,多条件查询时，必须把每个条件用（）括起来
    # filteredByOr = df[(df['99P PRN Price '] == 74.99) | (df['99P PRN Price '] <= 7.50)]
    # print(filteredByOr['99P PRN Price '])

    # 取指定的行和列:df.loc[行过滤表达式, 列过滤]
    # print(df.loc[df['Logistics Status '] == "Finished", 'Product '])

    # 取5-10行，3-5列
    # startIndex,endIndex不宝行
    # print(df.iloc[4:10, 2:5])

    # 改变第2-5行，第1列的值
    # df.iloc[1:5, 0] = 'Test'

    # air_quality = pd.read_csv('air_quality_no2.csv', index_col=0, parse_dates=True)
    # 根据已有列创建新列, 每行都会智能计算，不需要写循环
    # air_quality['london_mg_per_cubic'] = air_quality['station_london'] * 1.882
    # print(air_quality.head(10))

    # 重命名列 或行，
    # renamed = air_quality.rename(
    #     columns={
    #         'station_antwerp': 'BETR801',
    #         'station_paris': 'FR04014',
    #         'station_london': 'London Westminster'
    #     }
    # )
    # print(renamed)

    # 还可以传函数
    # print(renamed.rename(columns=str.lower))


def plots():
    """
    统计图
    :return:
    """
    # index_col设置指定列为行的index
    # parse_dates把列中的日期转为timestamp对象
    air_quality = pd.read_csv('air_quality_no2.csv', index_col=0, parse_dates=True)
    # print(air_quality.head(10))
    air_quality.plot()


if __name__ == '__main__':
    # df = pd.read_excel('test2.xlsx', sheet_name='Sales Report', header=2, usecols='A:CA')
    # 汇总统计
    # 平均数
    # print(df['CNF Price '].mean())

    # 总数
    # print(df[['CNF Price ', 'Purchase Price ']].sum())

    # 分析
    # print(df['CNF Price '].describe())

    # group by
    # 每个产品的数量
    # print(df[['Product ', 'CNF Price ']].groupby('Product ').sum())

    #  先groupby 再只看想看的数据
    # print(df.groupby('Product ')['Product '].count())

    # count by 记录类型,与上面的groupby结果一样
    # print(df['Product '].value_counts())


    # 排序：https://pandas.pydata.org/docs/user_guide/basics.html#basics-sorting
    air_quality = pd.read_csv('air_quality_no2.csv', index_col=0, parse_dates=True)
    # 按index排序
    # print(air_quality.sort_index(ascending=True).head())

    # 按某列的值排序
    # print(air_quality.sort_values(by='station_antwerp', ascending=False).head())

    # 按多列的值排序
    # print(air_quality.sort_values(by=['station_antwerp', 'station_london'], ascending=False).head())





