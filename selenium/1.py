# 要下载chrome驱动才能在IDE中打开对应浏览器：https://sites.google.com/a/chromium.org/chromedriver/downloads
import os
from selenium import webdriver
chromedriver = "D:\Anaconda3\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get('http://www.baidu.com')

