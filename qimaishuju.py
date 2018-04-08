#coding=utf-8
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
import json

def search_page():
    #访问页面
    driver = webdriver.Chrome()
    driver.get("https://www.qimai.cn/rank")

def roll():
    # 将页面滚动条拖到底部
    js = "var q=document.body.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(3)
    # 将滚动条移动到页面的顶部
    js = "var q=document.body.scrollTop=0"
    driver.execute_script(js)
    time.sleep(3)

def main():
    search_page()
    time.sleep(4)
    for i in range(1,5):
        roll()

if __name__ == '__main__':
    main()


''''' 
#若要对页面中的内嵌窗口中的滚动条进行操作，要先定位到该内嵌窗口，在进行滚动条操作 
js="var q=document.getElementById('id').scrollTop=100000" 
driver.execute_script(js) 
time.sleep(3) 
'''
