# -*- coding: utf-8 -*-
# @Time     :   2020/4/28 14:02
# @Author   :   Payne
# @File     :   Test3.py
# @Software :   PyCharm

"""基于selenium来获取cookies"""

from urllib.parse import urljoin
from selenium import webdriver
import requests
import time

BASE_URL = 'https://login2.scrape.cuiqingcai.com/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'
browser = webdriver.Chrome()
browser.get(BASE_URL)
browser.find_element_by_css_selector('input[name="username"]').send_keys(USERNAME)
browser.find_element_by_css_selector('input[name="password"]').send_keys(PASSWORD)
browser.find_element_by_css_selector('input[type="submit"]').click()
time.sleep(10)
cookies = browser.get_cookies()
print('Cookies:', cookies)
browser.close()

# set cookies to Requests
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])

response_index = session.get(INDEX_URL)

print('Response Status:', response_index.status_code)
print('Response URL', response_index.url)
print('Response Test:\n', response_index.text)