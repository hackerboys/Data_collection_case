# encoding:utf-8
from urllib.parse import urlencode
import requests
import json
import time
import os
import threading
import random

"""
功能解释点：

urlencode 功能就是 把字典数据的值 用 & 拼接在一起。具体详情，可以百度。
requeste 可以下载视频，音频，图片 更稳定点。


"""
# 48-24 = 24
HEADERS = {
    'cookie': 'sessionid=c950f19e-cfe2-4bd2-9456-79215f3dd14f; Hm_lvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1605366899; Hm_lpvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1605367321',
    'host': "www.duitang.com",
    'referer': 'https://www.duitang.com/search/?kw=%E5%8F%A4%E9%A3%8E%E5%A4%B4%E5%83%8F&type=feed',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

IMG_URL = []
DOWN_URLS = []
GLOCK = threading.Lock()

def main():

    for i in range(24, 3576 + 24, 24):
        currTimes = time.time()
        time_stamp = int(round(currTimes * 1000))
        url = 'https://www.duitang.com/napi/blog/list/by_search/?'
        parameters = {
            'kw': '古风头像',
            'type': 'feed',
            'include_fields': 'top_comments,is_root,source_link,item,buyable,root_id,status,like_count,like_id,sender,album,reply_count,favorite_blog_id',
            '_type': '',
            'start': i,
            '_': time_stamp,

        }
        urls = url + urlencode(parameters)
        IMG_URL.append(urls)

    for x in range(10): #  10多线程获取 请求的 url
        th = threading.Thread(target=producer)
        th.start()
    for x in range(10): #10多线程 下载
        th = threading.Thread(target=consumer)
        th.start()


def producer():
    while True:
        GLOCK.acquire()
        if len(IMG_URL) == 0:
            GLOCK.release()
            break
        urls = IMG_URL.pop()
        GLOCK.release()

        requ = requests.get(urls, headers=HEADERS)
        json_info = json.loads(requ.content)
        data = json_info['data']['object_list']
        for d in data:
            url_path = d["photo"]['path']
            DOWN_URLS.append(url_path)

def consumer():
    while True:
        GLOCK.acquire()
        if len(DOWN_URLS) == 0 and len(IMG_URL) == 0:
            GLOCK.release()
            break
        if len(DOWN_URLS)>0:
            down_url = DOWN_URLS.pop()
        else:
            down_url = ''

        GLOCK.release()

        number = random.sample(range(99, 100000000000000), 1)[0]
        new_number = random.sample(range(100000000000000, 1000000000000000), 1)[0] + number

        if not os.path.exists('古风头像/'):
            os.mkdir('古风头像/')
        if down_url:
            down_url = requests.get(down_url)
            with open("古风头像/%s.jpg" % (new_number), 'wb') as f:
                f.write(down_url.content)
                f.close()
                print("下载%s 图片完成" % new_number)



if __name__ == '__main__':
    main()