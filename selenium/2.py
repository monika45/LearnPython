# 下载phantomJS:https://phantomjs.org/download.html
from selenium import webdriver
drive = webdriver.PhantomJS(executable_path="D:\Anaconda3\Scripts\phantomjs.exe")
drive.get('http://www.baidu.com')
data = drive.title
print(data)

