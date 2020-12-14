#encoding:utf-8
from urllib.parse import urlencode
import requests
import json
import demjson
import time
import pandas as pd

headser = {
    'cookie':'__jdu=1702705520; areaId=18; ipLoc-djd=18-1574-3070-0; shshshfpa=25a6ee07-f876-6e3b-dc52-4ba9e1b2809b-1604924879; shshshfpb=rGiJ0pTaELHU%2FLvbP%2FrdwAQ%3D%3D; jwotest_product=99; JSESSIONID=C73727D19667AC55771D5C79DAEF9AC1.s1; unpl=V2_ZzNtbRdQFhAgW0dQLBkIBWILEQ4RAhFFIQtCBitNWldvB0JUclRCFnQURlRnGFQUZAEZXEBcRxBFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsfXQZhAhZZQVZzJXI4dmRzHVsNYwEiXHJWc1chVEVWeRxVBCoDFFxBUUIRcQtHZHopXw%3d%3d; __jda=76161171.1702705520.1604924877.1604934234.1604934236.4; __jdc=76161171; __jdb=76161171.2.1702705520|4.1604934236; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d6d4db05f1e1492bbdcae25cae7c95a8|1604934242281; shshshfp=4e92953ce37492278e84a231e8a2cf52; shshshsID=4c7d3dc7e9165860dc115f0f39cd6fee_3_1604934243135',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
}




nickname = [] # 用户名
referenceName = [] # 产品名称
productColor = [] # 产品规格
referenceTime = [] # 购买时间
comment_content = [] # 评论内容  content

for i in range(1,20):

    time.sleep(2)
    currTimes = time.time()
    time_stamp = int(round(currTimes * 1000))

    web_url = 'https://club.jd.com/comment/productPageComments.action?'
    parame = {
    # "callback": "jQuery1387989",
    "productId": "3950523",
    "score": "0",
    "sortType": "5",
    "page": i,
    "pageSize": "10",
    "pin": "null",
    "_": time_stamp,

    }



    urls =web_url + urlencode(parame)
    print(urls)
    html = requests.get(urls,headers=headser)
    jsontext = json.loads(html.content.decode('gbk').encode('utf-8'))
    # print(jsontext)
    comments = jsontext['comments']
    print(comments)
    for c in comments:
        username = c['nickname'] # 用户名
        product_name = c['referenceName'] #购买的产品名称
        product_spe = c['productColor'] # 购买的类型
        timetext  = c['referenceTime'] # 购买时间
        com_content = c['content'] # 评论内容

        nickname.append(username)
        referenceName.append(product_name)
        productColor.append(product_spe)
        referenceTime.append(timetext)
        comment_content.append(com_content)

excel_info = {'京东用户名称':nickname,'购买的产品名称':referenceName,'购买的产品规格':productColor,'购买时间':referenceTime,'评论内容':comment_content}
df = pd.DataFrame(excel_info,columns=['京东用户名称','购买的产品名称','购买的产品规格','购买时间','评论内容'])

df.to_excel("jd_kouhong.xlsx")