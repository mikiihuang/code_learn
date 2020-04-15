__author__ = 'yumihuang'
# project name:codelearn
# time:2020-03-30
import urllib.request as ur, re
import requests

class Spider():
    def __init__(self, word):
        self.word = word

    def openUrl(self, url):
        try:
            response = requests.get(url)
            return response.read()
        except:
            ... #在添加了tkinter界面时候写这里

    def searchWiki(self, html):
        r = re.search(r'<li class="item">▪<span class="selected">.*', html[self.end:])
        if(r == None):
            r = re.search(r'<li class="item">▪<a title=".*" href=\'/item/' + self.word + '/([0-9]|[a-z]|[A-Z]|[#])*\'>.*</a></li>',
                html[self.end:])
            if(r == None):
                return None
        self.now = r.start() + self.end
        self.end = r.end() + self.end
        return r

    def printMessage(self):
        if(self.nameUrl == dict()):
            print('没有搜到!')
            return
        if(len(self.nameUrl) == 1):
            return 0
        print('您所搜索的 %s 是一个多义词, 请选择:' % self.word)
        for each in self.nameUrl.keys():
            print(each)
        choose = int(input('请输入你想要搜索的序号: '))
        return choose

    def readWiki(self):
        #如果是多义词, 读取列表并提示用户选择
        html = requests.get('https://baike.baidu.com/item/' + self.word)
        print(html.text)
        self.now, self.end, self.nameUrl, count = 0, 0, dict(), 1
        #循环读取多义词意思
        while True:
            r = self.searchWiki(html)
            if(r == None):
                break
            #切割各个字段, url 是网址, name是意思
            line = html[self.now : self.end]
            namePos = re.search('(title=".*")|("selected">.*</span)', line)
            p = line[namePos.start() : namePos.end()]
            name = line[namePos.start() + 7 if 'tle' in p else namePos.start() + 11 :
                        namePos.end() - 1 if 'tle' in p else namePos.end() - 6]

            #切割各个网址
            url = 'https://baike.baidu.com' #原始网址
            urlPos = re.search('(href=\'/item/' + self.word + '/.*\')|(</span></li>)', line)
            if(line[urlPos.start() : urlPos.end()] == '</span></li>'):
                self.nameUrl['0) ' + name] = 'https://baike.baidu.com/search/word?word=' + self.word
                continue
            p = line[urlPos.start() : urlPos.end()]
            self.nameUrl[str(count) + ') ' + name] = url + p[6 : -1]
            count += 1
        self.choose = self.printMessage()
        self.readMessage()

    def readMessage(self):
        url = None
        if(self.choose == None):
            return
        for each in self.nameUrl.keys():
            if(str(self.choose) in each):
                url = self.nameUrl[each]
                break
        print(url)


if __name__ == '__main__':
    # word = str(input('输入你想要搜索的单词: '))
    c = Spider("黄疸")
    c.readWiki()