# encoding:utf-8
"""
作者：宋哈哈
代码说明：
    本页功能是，下载第1PPT模板网。
使用说明：
    1.请自行更改COOKIE
    2.下载地址等本地路径，请自行更换

"""



import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'cookie': 'UM_distinctid=1746215260c67-023eefee15a856-3323767-384000-1746215260d398; bdshare_firstime=1599373387369; CNZZDATA5092133=cnzz_eid%3D346151772-1599369427-null%26ntime%3D1599374827'
}


def class_ppt():
    "http://www.1ppt.com/moban/dongtai/"
    url = "http://www.1ppt.com/moban/"
    requ = requests.get(url, headers=headers)
    html = BeautifulSoup(requ.content, 'lxml')
    col_nav = html.find_all('div', class_="col_nav clearfix")
    for c in col_nav:

        a = c.find_all('a')
        for i in a:
            name = i.text
            filepath = "def_ppt/%s" % name
            # file = os.listdir("pptzipfile/%s"%name)
            if not os.path.exists(filepath):
                os.mkdir("def_ppt/%s" % name)
            else:
                class_url = "http://www.1ppt.com/" + i['href']
                # moban(class_url,name)
                "http://www.1ppt.com/moban/dongtai/ppt_dongtai_12.html"

                keystr = str(class_url).split('/')[5]
                for number in range(1, 200):
                    ppt_class_url = class_url + "ppt_" + keystr + "_" + str(number) + ".html"
                    print(ppt_class_url)
                    moban(ppt_class_url, name)

def moban(url, filepath):
    ppturl = "http://www.1ppt.com"
    requ = requests.get(url, headers=headers)
    html = BeautifulSoup(requ.content, 'lxml')
    h2 = html.find_all("h2")
    for h in h2:
        href = h.find_all("a")[0]['href']
        content_url = ppturl + href
        file = filepath
        ppt_content(content_url, file)


def ppt_content(url, file):
    # url = "http://www.1ppt.com/article/70088.html"
    requ = requests.get(url, headers=headers)
    html = BeautifulSoup(requ.content, 'lxml')
    ppt_title = str(html.find_all('h1')[0].text).replace('PPT模板免费下载', '').replace("/", '').replace('\\', '')
    downurllist = html.find_all("ul", class_="downurllist")
    for d in downurllist:
        downurl = d.find_all('a')[0]['href']
        print(downurl)
        requ_down_url = requests.get(downurl, headers=headers)
        urlretrieve(downurl, 'pptzipfile/%s/%s.zip' % (file, ppt_title))

if __name__ == '__main__':
    class_ppt()
