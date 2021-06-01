# 定位百度搜索框并自动搜索
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 启动驱动
chromedriver = "D:\Anaconda3\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('http://www.baidu.com')
# 断言，如果标题不包含“百度”就报错中断了
assert '百度' in driver.title
print(driver.title)

# 查找元素并输入内容
elem = driver.find_element_by_name('wd')
elem.send_keys('数据分析')
elem.send_keys(Keys.RETURN)

# 截图并退出
time.sleep(10)
driver.save_screenshot('baidu.png')
# 关闭页面
driver.close()
# 退出浏览器
driver.quit()

