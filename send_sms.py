"""发送短信"""
import urllib.parse
import http.client
import json


def main():
    host = '106.ihuyi.com'
    sms_send_uri = '/webservice/sms.php?method=Submit'
    params = urllib.parse.urlencode({
        'account': '****',
        'password': '***',
        'content': '测试发送短信',
        'mobile': '188********',
        'format': 'json'
    })
    print(params)
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain'
    }
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


if __name__ == '__main__':
    main()
