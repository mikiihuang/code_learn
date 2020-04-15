__author__ = 'yumihuang'
# project name:codelearn
# time:2020-04-11
import requests
from bs4 import BeautifulSoup
headers = {
            'user-agent': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36''',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate', 'accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'cache-control': 'max-age=0', 'connection': 'keep-alive',
            'referer': 'www.bing.com'
}
def get_html(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except:
        return None
    # response = requests.get(url,headers=headers)
    # print(response.text)


def parse_html(html):
    soup = BeautifulSoup(html,"lxml")
    all_movies = soup.find("ol",class_="grid_view").find_all("div",class_="item")

    # for data in all_movie.
    # items =
    movie_ll=[]
    for item in all_movies:
        movie_index = item.find("em").string
        movie_name =  item.find(class_="title").string
        movie_rating = item.find(class_="rating_num").string
        try:
            movie_desc = item.find(class_="inq").string
        except:
            movie_desc =""
        movie = "第"+movie_index+"部电影： "+movie_name+"     "+movie_rating+"      "+movie_desc
        movie_ll.append(movie)
    return movie_ll
def write_txt(content):
    with open("DouBanTOP250.txt","a",encoding="utf-8") as f:
        f.writelines([line+'\n' for line in content])
for i in range(10):
    url="https://movie.douban.com/top250?start="+str(25*i)+"&filter="
    movie_html = get_html(url)
    mm = parse_html(movie_html)
    write_txt(mm)
