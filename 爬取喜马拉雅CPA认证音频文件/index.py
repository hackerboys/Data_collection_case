#encoding:utf-8
import requests
import json
from bs4 import BeautifulSoup

headers = {
    "cookie": "_xmLog=h5&ac897f88-a0cb-4bd3-8ec0-8cf03cce13ad&2.1.2; x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1605019941,1607500522; Hm_lvt_dde6ba2851f3db0ddc415ce0f895822e=1607500527; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1607500822; Hm_lpvt_dde6ba2851f3db0ddc415ce0f895822e=1607500828",
    "referer": "https://www.ximalaya.com/jiaoyupeixun/38342442/300815186",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

}


def index():
    for i in range(1,3):
        url = 'https://www.ximalaya.com/jiaoyupeixun/38342442/p{}/'.format(i)

        requ = requests.get(url,headers=headers)
        html = BeautifulSoup(requ.content,'lxml')
        div = html.find_all("div",class_='text lF_')
        for d in div:
            title = d.find_all('span',class_='title lF_')[0].text

            ahref = str(d.find_all('a')[0]['href']).split('/')[-1]
            url_audio = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(ahref)
            json_data(url_audio,title)

def json_data(url,title):
    # url = 'https://www.ximalaya.com/revision/play/v1/audio?id=343098304&ptype=1'
    requ = requests.get(url,headers=headers)
    json_html = json.loads(requ.content)['data']['src']
    downurl = requests.get(json_html)

    with open("%s.m4a"%title,'wb')as f:
        f.write(downurl.content)
        f.close()
    print(f"{title},下载成功")

if __name__ == '__main__':
    index()