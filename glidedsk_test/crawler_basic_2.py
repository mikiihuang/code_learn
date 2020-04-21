__author__ = 'yumihuang'
# project name:codelearn
# time:2020-04-20

import requests
from bs4 import BeautifulSoup
import re
url = 'http://glidedsky.com/login'

h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
}
session = requests.session()
session.headers = h
token = session.get(url)
_token = re.search(r'"_token" value="(.*?)"', token.text).group(1)
print(_token)
data = {
    "_token": _token,
    "email": "",
    "password": "",
}
res = session.post(url, data=data, )



nums = 0
for page in range(1,1001):
    html = session.get("http://www.glidedsky.com/level/web/crawler-basic-2?page={}".format(str(page))).text
    bs = BeautifulSoup(html,"lxml")

    rows = bs.find_all("div",class_='col-md-1')

    for row in rows:
        num= int (row.get_text())
        # print(num)

        nums=nums+num
        # print(nums)
print(nums)