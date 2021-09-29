#!/usr/bin/env python
# coding=utf-8
import re
import os
import json
import lxml
import requests
from bs4 import BeautifulSoup

# 正在热映url
NOWPLAYING_URL= 'https://movie.douban.com/cinema/nowplaying/'

# 即将上映url
COMING_URL = 'https://movie.douban.com/coming'

# 豆瓣电影详情url
DETAIL_URL = 'https://movie.douban.com/subject/'

# 模拟请求头
HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'https://www.douban.com/'
}

# 电影实例list
movies = []

# 存入数据库总数
count = 0

# 代理ip类实例
proxyIps = ''


# 解析导演
def parseAuthor(dom):
        res = dom.find('a', rel='v:directedBy')
        return res.text if res else ''

# 解析时长
def parseDuration(dom):
        res = dom.find('span', property='v:runtime')
        return res.text if res else ''

# 解析类型
def parseTypes(dom):
        res = dom.find_all('span', property='v:genre')
        return [it.text for it in res]
        
# 解析类型
def parsePubdate(dom):
        res = dom.find('span', property='v:initialReleaseDate')
        return res.text if res else ''

# 解析类型
def parseRate(dom):
        res = dom.find('strong', property='v:average')
        return res.text if res else 0

# 解析类型
def parseSummary(dom):
        res = dom.find('span', property='v:summary')
        return res.text.strip() if res else ''


def crawlAttr(movie):
        """
        爬取电影详情页获取预告片
        """
        #print('爬取ID: %s, Title: %s' % (movie["id"], movie["data-title"]))
        url = DETAIL_URL + movie["id"]
        movie["url"]=url
        for i in range(2):
                try:
                        r = requests.get(url, headers=HEADERS, timeout=30).text
                        info = BeautifulSoup(r, 'lxml').select_one('div#info')
                        movie["movieTypes"] = parseTypes(info)
                        movie["pubdate"] = parsePubdate(info)
                        summaryDom = BeautifulSoup(r, 'lxml').select_one('div#link-report')
                        movie["summary"] = parseSummary(summaryDom) if summaryDom else ''
                except Exception:
                        print('超时或被禁: %s' %  movie["id"])
                        continue
                with open(f'message/{movie["id"]}.txt',"w") as f:
                    msg=""
                    for item in ["id","pubdate","data-title","data-duration","data-region","movieTypes","data-director","data-actors","data-score","summary","url"]:
                        try:
                            info=movie[item].replace("\n","")
                            msg+=f'[{item}]:\t{info}\n'
                        except:continue
                    print(msg)
                    f.write(msg)
                break


def beginCrawl(movies=dict):
        """
        遍历待爬取电影数组，获取所有属性，存入数据库
        """
        for idx, movie in enumerate(movies.keys()):
                crawlAttr(movies[movie])


def main():
        """
        爬虫入口，获取要爬取的电影doubanID
        """
        movies={}
        r = requests.get(NOWPLAYING_URL, headers=HEADERS, timeout=10).text
        for sel in ["div#nowplaying li.list-item","div#upcoming li.list-item"]:
                lists = BeautifulSoup(r, 'lxml').select(sel)
                for l in lists:
                        movies[l["id"]]={}
                        for item in ["id","data-title","data-duration","data-region","data-director","data-actors","data-score"]:
                                        try:movies[l["id"]][item]=l[item]
                                        except:continue
        print('***************已获取待爬取电影数组:  %s个***************' % len(movies.keys()))
        beginCrawl(movies)



if __name__ == '__main__':

    try:os.mkdir("message")
    except:pass
    main()
