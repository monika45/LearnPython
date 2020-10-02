from urllib import request
from urllib import parse
from http.cookiejar import CookieJar
import json


def use_urllib():
    resp = request.urlopen('https://www.sogou.com')
    # resp.read() resp.getcode() resp.readline()
    print(resp.read())
    print(resp.info())

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

    url = 'http://www.test.com?a=123&b=456&c=测试'
    query_data = {
        'a': 123,
        'b': 456,
        'c': '测试'
    }
    # 对一个字典进行urlencode
    query = parse.urlencode(query_data)
    print(query)
    # 对字符串进行urlencode
    print(parse.quote('测试'))
    # 解码
    print(parse.parse_qs(parse.quote('测试')))
    # url解析
    print(parse.urlparse(url))


def maoyanpiaofang():
    url = 'http://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=174e1b2906dc8-04f28bd602d3fb-5b123211-1fa400' \
          '-174e1b2906dc8&riskLevel=71&optimusCode=10&_token=eJxF0ktrwzAMAOD' \
          '%2ForNJLcuPJNBDYTAy2GGl26X04L7SMpqUNIyNsf8%2BeVpjCPiLsB4R' \
          '%2BYah2UOtFXwcBqgBC114UDDeoEav0aG1riTjFexyzHvjgzcKtsPbA9RrxGBURWGTIksOrLEyWqEu9UbdbdnG8pNuNXwJTuN4rWez6zn2x9i1xSX2X7Erdv1lto%2B307aPw55nAU64rFIC90FlKstBRO%2BYTqiZ4Y8uMEuhzUxplVBPtEGRRqHPtEwjxIlUMUmY0qQxuUxihkxpTFwBtVAzpZgpmfIVhouhpPGSCWUyw3UNZlKmy%2FSZZWY11aXcmHAanVxa6HtaKJ%2Fx%2Fxzv78%2F8F%2FDd27ntWIenz9Vr2ywWj%2B1i%2BTKfw88vSdB55g%3D%3D '
    headers = {
        'Referer': 'http://piaofang.maoyan.com/dashboard',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'X-FOR-WITH': 'PbUS6x1Ic8mwlHJUKwVxaUeJgzQulreGofcsL0N+RJV8bJ4OfCB5UTfYmSuXObACRSgV+cauBjAns07Q5xpXYjtjLQJuDLlosYHrqRtjaxbPJk2JLdGWzi1hL84AhOoTyIBI1ZTdgRZSJLROA3PGDcLbfppc3ypE/jSkx/RYWVaS8a9WAWCm2Nb7hVbtv3o4qAyh7bh8LEgIzulyu7wFJw='
    }
    rq = request.Request(url, headers=headers)
    resp = request.urlopen(rq)
    if resp.getcode() != 200:
        print('获取失败')
    else:
        data = resp.read().decode('utf-8')
        print(data)
        json_data = json.loads(data)
        print(json_data['movieList'])


def useProxyHandler():
    """使用代理"""
    url = 'https://www.test.com'
    handler = request.ProxyHandler({'http': '代理IP:端口'})
    opener = request.build_opener(handler)
    resp = opener.open(url)
    print(resp.read())


def login_zhihu():
    login_url = 'https://i.meishi.cc/login_t.php?username=18580229220&login_type=2&password=f2461061&cookietime=on'
    mine_url = 'https://i.meishi.cc/jifen/mingxi.php'
    username = '*****'
    password = '****'
    cookiejar = CookieJar()
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    rq = request.Request()

if __name__ == '__main__':
    maoyanpiaofang()