from urllib import request

# resp = request.urlopen('https://www.sogou.com')
# # resp.read() resp.getcode() resp.readline()
# print(resp.read())
# print(resp.info())

# 用request可以设置请求头
url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/77.0.3865.90 Safari/537.36 '
}
rq = request.Request(url, headers=headers)
resp = request.urlopen(rq)
data = resp.read()
# 写的时候自动按encoding编码为bytes
# file = open('../res/1.html', 'w', encoding='utf-8')
# file.write(data.decode('utf-8'))
file = open('../res/1.html', 'wb')
file.write(data)
file.close()
# print(data.decode('utf-8'))
# 读的时候自动按encoding解码
print(open('../res/1.html', 'r', encoding='utf-8').read())


