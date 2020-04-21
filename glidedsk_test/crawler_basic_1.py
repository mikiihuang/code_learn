__author__ = 'yumihuang'
# project name:codelearn
# time:2020-04-19
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


headers = {'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
           'x-client-data':"CIi2yQEIprbJAQjBtskBCKmdygEIy67KAQjQr8oBCLywygEIl7XKAQjttcoBCI66ygEYu7rKARjavcoB"}
html = session.get("http://www.glidedsky.com/level/web/crawler-basic-1").text
bs = BeautifulSoup(html,"lxml")

rows = bs.find_all("div",class_='col-md-1')
nums = 0
for row in rows:
    num= int (row.get_text())
    nums=nums+num
print(nums)