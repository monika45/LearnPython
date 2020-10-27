"""爬虫数据提取"""
import requests
from lxml import etree


def lxml_usage():
    """使用lxml解析html和文件"""
    str = '''
        <ul>
            <li class="item-1">aaaaa<span>1a1</span><a class="a-1">1111</a></li>
            <li class="item-2"><a class="a-2">2222</a>bbbbb<span>2a2</span></li>
            <li class="item-3" href="http://test.com"><a class="a-3">3333</a>ccc</li>
            <li class="item-4">dddd<a class="a-4">4444</a></li>
            <li class="item-5">eeee</li>
            <li class="item-6">ffff
        </ul>
    
    '''
    # 文本解析为html（etree会自动补全缺失的html标签，修正语法错误）
    html = etree.HTML(str)

    with open('../res/1.html', 'wb') as file:
        file.write(etree.tostring(html))

    # print(html)
    result = etree.tostring(html).decode('utf-8')
    # print(result)

    # 从文件中读取html内容
    html = etree.parse('../res/1.html')
    result = etree.tostring(html, pretty_print=True)
    # print(result)


def xpath_use():
    """使用xpath语法提取数据"""
    html = etree.parse('../res/1.html')
    # 获取所有li标签
    result = html.xpath('//li')
    # print(result)
    # for ele in result:
    # print(etree.tostring(ele).decode('utf-8'))

    # 获取所有li标签的class属性
    result = html.xpath('//li/@class')
    # print(result)

    # 获取class为item-2的li标签
    result = html.xpath('//li[@class="item-2"]')
    # print([etree.tostring(li) for li in result])

    # 获取li标签下href为test.com的标签
    result = html.xpath('//li/a[@href="http://test.com"]')
    # print([etree.tostring(a) for a in result])

    # 获取li标签下的class为i-1的i标签
    result = html.xpath('//li/a/i[@class="i-1"]')
    result2 = html.xpath('//li//i[@class="i-1"]')
    # print(result)
    # print([etree.tostring(i) for i in result])

    # 获取li标签下a标签里的所有的class
    result = html.xpath('//li/a/@class')
    # 获取li标签下a标签下的所有的class，包括a的class和a的子孙节点的class
    result2 = html.xpath('//li/a//@class')
    # print(result)
    # print(result2)

    # 获取最后一个li下的a的href属性值
    result = html.xpath('//li[last()]/a/@href')
    # print(result)

    # 获取倒数第二个li里面的内容
    result = html.xpath('//li[last()-1]/span')
    print(result)
    print(result[0].text)
    result2 = html.xpath('//li[last()-1]/span/text()')
    print(result2)


def grab_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Cookie': 'uuid=fe6b2009-bc37-492f-8ffd-f7a017d19939; cityDomain=cq; clueSourceCode=%2A%2300; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1602322327; ganji_uuid=7890730954232877310267; sessionid=08d52466-6d41-4b6e-9f7c-7a0e971aa037; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22fe6b2009-bc37-492f-8ffd-f7a017d19939%22%2C%22ca_city%22%3A%22cq%22%2C%22sessionid%22%3A%2208d52466-6d41-4b6e-9f7c-7a0e971aa037%22%7D; preTime=%7B%22last%22%3A1602323045%2C%22this%22%3A1602322325%2C%22pre%22%3A1602322325%7D; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1602478073; rfnl=https://www.guazi.com/cq/?ca_kw&ca_n=default&ca_s=seo_baidu; antipas=6447C70gr15H1p830521V66d621'
    }
    url = 'https://www.guazi.com/cq/bmw/'
    detail_urls = get_detail_urls(url, headers)
    carlist = []
    for detail_url in detail_urls:
        carinfo = parse_detail_page(detail_url, headers)
        carlist.append(carinfo)
    print(carlist)


def get_detail_urls(url, headers):
    """获取详情页urls"""
    data = requests.get(url, headers=headers)
    html = etree.HTML(data.content.decode('utf-8'))
    # print(print(html))
    ul = html.xpath('//ul[@class="carlist clearfix js-top"]')[0]
    # print(etree.tostring(ul[0]))
    lis = ul.xpath('./li')
    # print(lis)
    detail_urls = []
    for li in lis:
        detail_url = 'https://www.guazi.com' + li.xpath('./a/@href')[0]
        detail_urls.append(detail_url)
    return detail_urls


def parse_detail_page(detail_url, headers):
    """解析详情页内容"""
    data = requests.get(detail_url, headers=headers)
    html = etree.HTML(data.content.decode('utf-8'))
    # print(etree.tostring(html).decode('utf-8'))
    carinfo = {}
    main_data = html.xpath('//div[@class="product-textbox"]')[0]
    carinfo['title'] = main_data.xpath('./h2[@class="titlebox"]/text()')[0].replace(r'\r\n', '').strip()
    info = main_data.xpath('./ul[@class="assort clearfix"]/li/span/text()')
    carinfo['miles'] = info[2]
    carinfo['displacement'] = info[3]
    carinfo['speedbox'] = info[4]
    carinfo['price'] = main_data.xpath('.//div[@class="price-main"]/span/text()')[0]
    return carinfo


if __name__ == '__main__':
    grab_data()
