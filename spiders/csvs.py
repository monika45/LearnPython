import csv
import random

headers = ['姓名', '语文', '数学', '英语']
first_names = '赵钱孙李王陆曾吴印余俞于曹刘甄林贾丁陈朱张贺彭尹何罗'
last_names = '玉鱼雨闻文果清青期数床前明月光三期大非九天魅族得无玫瑰麦克'
filename = '../res/成绩表.csv'


def create_name():
    """随机生成姓名"""
    return random.choice(first_names) + ''.join(random.sample(last_names, 2))


def writerow():
    """writerow()方式写入"""
    students = []
    for i in range(0, 20):
        students.append((create_name(), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)))
    print(students)
    with open(filename, 'w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(students)


def dict_write():
    """使用dictWriter"""
    students = []
    for i in range(0, 20):
        students.append({
            headers[0]: create_name(),
            headers[1]: random.randint(1, 100),
            headers[2]: random.randint(1, 100),
            headers[3]: random.randint(1, 100)
        })
    # print(students)
    with open(filename, 'w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()
        writer.writerows(students)


if __name__ == '__main__':
    dict_write()
    