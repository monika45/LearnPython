"""
xpath 练习
"""

import requests
from lxml import html
import re


url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
pageContent = requests.get(url, headers=headers)
tree = html.fromstring(pageContent.content)

# 从文件读取
# tree = html.fromstring(open('test.html', 'rb').read())

content = tree.xpath('//div[@id="content"]')[0]
# print(html.tostring(content))


# 解析出结果，按某个键值排序
movies = []
items = content.xpath('.//div[@class="item"]')
for item in items:
    year_and_type = html.tostring(item.xpath('.//div[@class="bd"]/p')[0], pretty_print=True, encoding='utf-8').decode('utf-8').split('<br>')[1].strip()
    yt = year_and_type.replace('</p>', '').strip().split('\xa0/\xa0')
    movie_info = {
        'pic': item.xpath('div[@class="pic"]//img/@src')[0],
        'detail_url': item.xpath('div[@class="pic"]/a/@href')[0],
        'title': [i.strip('\xa0/\xa0') for i in item.xpath('div[@class="info"]/div[@class="hd"]/a/span/text()')],
        'director': item.xpath('.//div[@class="bd"]/p/text()')[0].strip(),
        'year': yt[0],
        'country': yt[1],
        'type': yt[2],
        'star': item.xpath('.//div[@class="star"]/span[2]/text()')[0],
        'comment_num': item.xpath('.//div[@class="star"]/span[4]/text()')[0].replace('人评价', ''),
        'quote': item.xpath('.//p[@class="quote"]/span/text()')[0]
    }
    # print(movie_info)
    # break
    movies.append(movie_info)

print(movies)
