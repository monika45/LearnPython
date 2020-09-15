"""正则表达式"""
import re

str1 = 'This is a big pie.I will teach you how to make it.It is delicious ' \
       'Tel:18023456785 and QQ: 8424322 . <eee>'


# while True:
#     username = input('请输入用户名：')
# 用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
# m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
# m1 = re.match(r'^\w{6,20}$', username)
# print(m1)
#     print(re.match(r'(?<=\W)(big)(?=\W)', username))
# pattern = re.compile(r'(?<=\D)1[0-9]\d{9}(?=\D)')
# print(re.findall(pattern, str1))
# print(re.findall(r'w\w{2}l', str1))
# print(re.finditer(r'w\w{2}l', str1))
# print(pattern.search(str1).group())

# 替换字符串中的内容
# s = re.sub(r'(?<=Tel:)\d{11}', '***********', str1, flags=re.I | re.M)
# print(s)


def spilt_str():
    """拆分长字符串"""
    poem = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[,，.。]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)


# print(spilt_str())


