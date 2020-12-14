# encoding:utf-8
# url = http://www.51kids.com/Join/
"""
爬取 http://www.61ef.cn/brand/list-15-0-0-0-0-1.html 资料


"""


import requests
from bs4 import BeautifulSoup
from filepdfs import pdf_htmlfile # 导入转PDF，已经写好，请设置 Sources Root
import re
from pyquery import PyQuery
import time
Headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    "cookie":'__cfduid=d1b2547ae15545360ff2eda42b07d2a351599131653; Hm_lvt_8a5512b423c7f0d2c8543d145073903f=1599131657; ASP.NET_SessionId=d0nzjtqe4uvhlp2y5ofvyhzu; Hm_lpvt_8a5512b423c7f0d2c8543d145073903f=1599134429'
}


def tzblank_url():
    for n in range(1,916):
        time.sleep(2)
        url = "http://www.61ef.cn/brand/list-15-0-0-0-0-{}.html".format(n)
        print(url)
        requ = requests.get(url,headers=Headers)
        html = BeautifulSoup(requ.content,'lxml')
        li = html.find_all('li',class_='compamy_content3')
        for l in li:
            web = "http://www.61ef.cn/"
            a = str(l.find_all('a')[0]['href']).replace('#msgnew','')
            blank_url = web+a # 品牌网页链接
            num_url = str(blank_url).split('-')[1].split('.')[0]
            tzblank_content(num_url)

def tzblank_content(num):
    "http://www.61ef.cn/brand/show-37031.html" #主页链接
    "http://www.61ef.cn/brand/company-37031.html" # 公司简介
    "http://www.61ef.cn/brand/brand-37031.html"# 品牌简介
    "http://www.61ef.cn/brand/jiameng-37031.html" #加盟规则
    "http://www.61ef.cn/brand/product-37031-1.html" # 产品展示
    "http://www.61ef.cn/brand/shop-37031-1.html"# 店铺形象
    try:
        show_url = "http://www.61ef.cn/brand/show-{}.html".format(num)
        # show_url = "http://www.61ef.cn/brand/show-36023.html"
        requ_show = requests.get(show_url,headers = Headers)
        html_show = BeautifulSoup(requ_show.content,'lxml')
        blank_name = html_show.find_all('div',class_='brandLogo')[0].find_all('img')[0]['alt']+"童装"


        keylist = ["company","brand","jiameng"]
        newlist_contnet = []
        for k in keylist:
            url = "http://www.61ef.cn/brand/{}-{}.html".format(k,num)

            requ = requests.get(url, headers=Headers)
            html = BeautifulSoup(requ.content, 'lxml')
            content_html = str(html.find_all("div",class_="borderColor brandDiv")[0])
            a = r'\<a.*?\>.*?\</a\>'
            news = re.compile(a,re.S)
            content = news.sub('',content_html)
            newlist_contnet.append(content)
        keylis_ps = ["product", "shop"]
        for kp in keylis_ps:
            url_ps =  "http://www.61ef.cn/brand/{}-{}-1.html".format(kp,num)
            requ_ps = requests.get(url_ps, headers=Headers)
            html_ps = BeautifulSoup(requ_ps.content, 'lxml')
            content_ps = html_ps.find_all("div", class_="borderColor brandDiv")[0]
            # print(content_ps)
            aps = r'\<a.*?\>'
            news_ps = re.compile(aps, re.S)
            newps_content = news_ps.sub('', str(content_ps))
            pq_content = PyQuery(str(newps_content))
            pq_content('.page').remove()
            newlist_contnet.append(pq_content)

        sethtlm = ''.join('%s' %id for id in newlist_contnet)
        charsetstr  = '<head><meta charset="UTF-8"> </head>'
        newhtml = charsetstr + sethtlm

        with open("html/%s.html"%blank_name,'w',encoding='utf-8') as f:
            f.write(newhtml)
            f.close()
            print('写入成功')

        pdf_htmlfile(blank_name,"html/%s.html"%blank_name,"pdf")
    except:
        pass


if __name__ == '__main__':
    tzblank_url()
