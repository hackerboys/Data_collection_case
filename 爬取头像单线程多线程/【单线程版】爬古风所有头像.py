#encoding:utf-8
from urllib.parse import urlencode
import requests
import json
import time
import os
import random



"""
功能解释点：

urlencode 功能就是 把字典数据的值 用 & 拼接在一起。具体详情，可以百度。
requeste 可以下载视频，音频，图片 更稳定点。


"""
# 48-24 = 24
HEADERS = {
    'cookie':'sessionid=c950f19e-cfe2-4bd2-9456-79215f3dd14f; Hm_lvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1605366899; Hm_lpvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1605367321',
    'host':"www.duitang.com",
    'referer':'https://www.duitang.com/search/?kw=%E5%8F%A4%E9%A3%8E%E5%A4%B4%E5%83%8F&type=feed',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}


def index():
    """
    这里得到是一个 json 文件的 url 。

    改变url = https://www.duitang.com/search/?kw=%E5%8F%A4%E9%A3%8E%E5%A4%B4%E5%83%8F&type=feed#!s-p30  最后的 p30 得到 第三十页 利用手工往下拉，手工获取到 start 的最大值 为 3576 ,方便些 for 循环
    :return:
    """

    for i in range(24,3576+24,24): # 从24 开始  以 24 增加，一直到 3576 ，为啥要加 24 ？可以考下学生。
        # print(i)

        # time.sleep(2) # 延迟2秒，显得更人为操作去获取url .
        currTimes = time.time()
        time_stamp = int(round(currTimes * 1000)) # 获取到 毫秒

        url = 'https://www.duitang.com/napi/blog/list/by_search/?'
        parameters = {

        'kw': '古风头像',
        'type': 'feed',
        'include_fields': 'top_comments,is_root,source_link,item,buyable,root_id,status,like_count,like_id,sender,album,reply_count,favorite_blog_id',
        '_type':'',
        'start': i, # 把 for 循环替换到这里
        '_': time_stamp, # 时间戳到毫秒的,

        }
        urls =url + urlencode(parameters) # 拼接 parameters 字典的值
        print(urls)
        # print(urls)
        requ = requests.get(urls,headers=HEADERS)
        json_info= json.loads(requ.content) # 直接打印会报错，和自己pycharm 设置的编码格式有关系，因为文件中出现表情等信息，pycharm 设置的 gbk 无法打印，要设置 UTF-8。具体需要实验。
        # 整理 json 数据的网站有：https://www.json.cn/#  https://www.sojson.com/

        data = json_info['data']['object_list']
        for d in data:
            url_path = d["photo"]['path'] # 直接获取到头像 图片的 url
            number = random.sample(range(99, 100000000000000), 1)[0]
            new_number = random.sample(range(100000000000001, 1000000000000000), 1)[0] + number # 减少随机数重复概率 让两个不同范围的随机数相加。

            print("下载%s 图片中..." % new_number)
            download(new_number,url_path)

def download(img_name,img_url):
    """
    下载图片
    :return:
    """
    if not os.path.exists('古风头像/'):
        os.mkdir('古风头像/')
    down_url  = requests.get(img_url)
    with open("古风头像/%s.jpg"%(img_name),'wb') as f:
        f.write(down_url.content)
        f.close()



if __name__ == '__main__':
    index()

