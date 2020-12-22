# encoding:utf-8
import sys
import requests
import json
import threading
import redis
from User_Agents import ua
from ipagent import agent
import traceback
from update_pagenumber import *

sys.path.append(r'D:\PythonPro\DataCollection36\test\lcsc.com') # 请修改环境变量路径，路径是本爬虫目录路径

redis_data = redis.StrictRedis(host="localhost", port=6379, db=12)  # 库存不为 0 的
redis_no_data = redis.StrictRedis(host="localhost", port=6379, db=13)  # 库存为 0 的

Form_data_list = []
GLOCK = threading.Lock()


def page_url():
    headers = {

        "cookie": "CASAuth=2naldnduock3de36a3toq585ll; currency_symbol=US%24; _ga=GA1.2.1967328765.1607657137; _gid=GA1.2.1523443700.1607657137; _fbp=fb.1.1607657143014.1603377610; Hm_lvt_dde6ba2851f3db0ddc415ce0f895822e=1607657144,1607778948; ONEAPM_BI_sessionid=4120.452|1607794612561; _gat_UA-98399433-1=1; Hm_lpvt_dde6ba2851f3db0ddc415ce0f895822e=1607799668; track=eyJpdiI6IktWTTlIdFhTK01JUlIrN3k2Q1NhSWc9PSIsInZhbHVlIjoiUnpIRTVzelwvVlBpVHJyOVRQdTRKMVdBN3hKRXZQVFwvYWdyVmlpWEtMdmJHcnFJXC9malNJVkRCSzlla3gwaG80VWdVSkFWakRFM2t6bVN1TnZYRWtoRlFVSHNuQlplMkVcLzdTSGNYNXhqbWJvb29JXC9KN2s5ZmRTMEtPOGpqTUtIR1NIXC8xQSt4ZVhcL1p3aFJaYkl5eVVIRGwrakNoYmhlSU1obFVMU2diRUMybUQ4Q1QxSGlkc0pNUWk1cWRBb0ZmNTh6d3dpMFM1THBma1FWVkVDSFZ6Y1wvU3dUN3N6dXdLYVhvNzBESzlWZWFRY290SjVpek5GMUhsSENtSXl1SEoxIiwibWFjIjoiMmE5NDAwZGJiYmRjYjk4ZmRlNzFmMzYzMDk5ODU3ZGNiNzc1OWQwMjI0Zjg2OGE5NmQ4MDAzYjJjOGQ1ZmQzOSJ9; XSRF-TOKEN=eyJpdiI6IlVMNDZzTSt6bkdrQVNGdDVzMXVRSEE9PSIsInZhbHVlIjoiNW90aWJPZ041Sm5DbFZpakJwNW1BK1BFVjNXS2dqa1wvNk1tVmREVDNPT3cxRjZnMk55Nnd1alc5NUt4aHRcL3pCZzVSOWtZbjh5ZjlLMVwvbzl2UzYrSUE9PSIsIm1hYyI6IjVmZmUxNjMzZGU3NDMwZTI1NjBjNDk0ODZlOWM2MDhiMzA4NzM3ZGUxZDA5Mzg3N2M4MGI0YjViMGZjZDhkMWYifQ%3D%3D; lcsc_session=eyJpdiI6IlwvTVZWSFwvZUwxRDJkNTdBNzI0NTFoZz09IiwidmFsdWUiOiJDOWFjNmtYXC9wVmhqZjFNZWlIdTl0MVZEQ3pmTld3UmZaa0FRazE1Y3FFcjNuNytUN2F2QStzcU1EMzBLcVZleXorWE03a0lpNUhsdDRuK21zZEJEVHc9PSIsIm1hYyI6ImVkMjRhNmM4NjBmM2VhOTc3NWQ0NDEzMzI2ODVlY2Q1N2QzNDEzNDhkNzdlMDMzYWZlOGE1ZWIxMTI2MTc3YzcifQ%3D%3D; currency=eyJpdiI6ImhQXC83aFFHb2MrUUdFNWI2bVh5ZnVRPT0iLCJ2YWx1ZSI6IjBlVlRHNWhRTHQra0w0ejlhMHJqc0lPY1ZlMnpjZXArNGFJSHd4OTNDTUtzU2VCXC9FaWdVSlpxd3ZtZDJCVnkzQmlOSzBYRGxZZW5tM2xJN1o5TkZ1cWpkSHZzRUM3dGkwdkNSZzM5WFltUnpDRVV3V0NJWXZtRHNYYjFFa1VNc2JQWGM4bDdnTFwvWVl0bHhIbVAwSXB3PT0iLCJtYWMiOiJkOTUyNTI1YmMwYTNmN2I0Yzk3NjBiMWNhNDVmNzM0ZGY1ZjZlOTFlZmYyYWJjZjZlYzU5MjBhYTI2YzdlYmY4In0%3D",
        "isajax": "true",
        "origin": "https://lcsc.com",
        "referer": "https://lcsc.com/products/Connectors_365.html",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "%s" % ua,
        "x-csrf-token": "NOWGfXddJdJjvfxMp0Kcw0R0LV1xbY0EtYYzhO0v",
        "x-requested-with": "XMLHttpRequest",
    }
    url = "https://lcsc.com/api/products/search"
    datas = {
        "current_page": "2",
        "category": "365",
        "in_stock": "false",
        "is_RoHS": "false",
        "show_icon": "false",
        "search_content": "",
        "limit": "25"
    }

    proxies = {
        'https': 'https://{}'.format(agent())
    }
    # print(f"当前是{proxies} 正在发送请求")
    respon_data = requests.post(url, data=datas, proxies=proxies, headers=headers, timeout=5,
                                allow_redirects=False)

    json_content = json.loads(respon_data.content)['result']['last_page']
    return json_content


def requests_info():
    while True:
        GLOCK.acquire()
        if len(Form_data_list) == 0:
            GLOCK.release()
            break
        GLOCK.release()
        form_data = Form_data_list.pop()
        headers = {

            "cookie": "CASAuth=2naldnduock3de36a3toq585ll; currency_symbol=US%24; _ga=GA1.2.1967328765.1607657137; _gid=GA1.2.1523443700.1607657137; _fbp=fb.1.1607657143014.1603377610; Hm_lvt_dde6ba2851f3db0ddc415ce0f895822e=1607657144,1607778948; ONEAPM_BI_sessionid=4120.452|1607794612561; _gat_UA-98399433-1=1; Hm_lpvt_dde6ba2851f3db0ddc415ce0f895822e=1607799668; track=eyJpdiI6IktWTTlIdFhTK01JUlIrN3k2Q1NhSWc9PSIsInZhbHVlIjoiUnpIRTVzelwvVlBpVHJyOVRQdTRKMVdBN3hKRXZQVFwvYWdyVmlpWEtMdmJHcnFJXC9malNJVkRCSzlla3gwaG80VWdVSkFWakRFM2t6bVN1TnZYRWtoRlFVSHNuQlplMkVcLzdTSGNYNXhqbWJvb29JXC9KN2s5ZmRTMEtPOGpqTUtIR1NIXC8xQSt4ZVhcL1p3aFJaYkl5eVVIRGwrakNoYmhlSU1obFVMU2diRUMybUQ4Q1QxSGlkc0pNUWk1cWRBb0ZmNTh6d3dpMFM1THBma1FWVkVDSFZ6Y1wvU3dUN3N6dXdLYVhvNzBESzlWZWFRY290SjVpek5GMUhsSENtSXl1SEoxIiwibWFjIjoiMmE5NDAwZGJiYmRjYjk4ZmRlNzFmMzYzMDk5ODU3ZGNiNzc1OWQwMjI0Zjg2OGE5NmQ4MDAzYjJjOGQ1ZmQzOSJ9; XSRF-TOKEN=eyJpdiI6IlVMNDZzTSt6bkdrQVNGdDVzMXVRSEE9PSIsInZhbHVlIjoiNW90aWJPZ041Sm5DbFZpakJwNW1BK1BFVjNXS2dqa1wvNk1tVmREVDNPT3cxRjZnMk55Nnd1alc5NUt4aHRcL3pCZzVSOWtZbjh5ZjlLMVwvbzl2UzYrSUE9PSIsIm1hYyI6IjVmZmUxNjMzZGU3NDMwZTI1NjBjNDk0ODZlOWM2MDhiMzA4NzM3ZGUxZDA5Mzg3N2M4MGI0YjViMGZjZDhkMWYifQ%3D%3D; lcsc_session=eyJpdiI6IlwvTVZWSFwvZUwxRDJkNTdBNzI0NTFoZz09IiwidmFsdWUiOiJDOWFjNmtYXC9wVmhqZjFNZWlIdTl0MVZEQ3pmTld3UmZaa0FRazE1Y3FFcjNuNytUN2F2QStzcU1EMzBLcVZleXorWE03a0lpNUhsdDRuK21zZEJEVHc9PSIsIm1hYyI6ImVkMjRhNmM4NjBmM2VhOTc3NWQ0NDEzMzI2ODVlY2Q1N2QzNDEzNDhkNzdlMDMzYWZlOGE1ZWIxMTI2MTc3YzcifQ%3D%3D; currency=eyJpdiI6ImhQXC83aFFHb2MrUUdFNWI2bVh5ZnVRPT0iLCJ2YWx1ZSI6IjBlVlRHNWhRTHQra0w0ejlhMHJqc0lPY1ZlMnpjZXArNGFJSHd4OTNDTUtzU2VCXC9FaWdVSlpxd3ZtZDJCVnkzQmlOSzBYRGxZZW5tM2xJN1o5TkZ1cWpkSHZzRUM3dGkwdkNSZzM5WFltUnpDRVV3V0NJWXZtRHNYYjFFa1VNc2JQWGM4bDdnTFwvWVl0bHhIbVAwSXB3PT0iLCJtYWMiOiJkOTUyNTI1YmMwYTNmN2I0Yzk3NjBiMWNhNDVmNzM0ZGY1ZjZlOTFlZmYyYWJjZjZlYzU5MjBhYTI2YzdlYmY4In0%3D",
            "isajax": "true",
            "origin": "https://lcsc.com",
            "referer": "https://lcsc.com/products/Connectors_365.html",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "%s" % ua,
            "x-csrf-token": "NOWGfXddJdJjvfxMp0Kcw0R0LV1xbY0EtYYzhO0v",
            "x-requested-with": "XMLHttpRequest",
        }
        url = "https://lcsc.com/api/products/search"
        ip_data = agent()
        proxies = {
            'https': 'https://{}'.format(ip_data)
        }
        print(f"当前是{proxies} 正在发送请求")
        try:

            respon_data = requests.post(url, data=form_data, proxies=proxies, headers=headers, timeout=5,
                                        allow_redirects=False)

            json_content = json.loads(respon_data.content)
            if json_content['success'] == True:
                Downdata(json_content)

                print(f"第 {json_content['result']['current_page']} 页，获取到数据！")

            if json_content['success'] == False:
                agent()
                Form_data_list.insert(0, form_data)
                print(f"第 {json_content['result']['current_page']} 页，请求数据成功,未获取到数据！")

        except:
            Form_data_list.insert(0, form_data)

            with open('error.log', "a") as f:
                traceback.print_exc(file=f)


def Downdata(json_data):
    pb_list = []

    json_content = json_data['result']['data']
    current_page = json_data['result']['current_page']  # 页码

    print("************************************")
    print(f"获取到第 {current_page} 页正在写入数据库中")
    print("************************************")
    update_page(current_page)


    for jd in json_content:

        c_number = jd['number']  # LCSC_PART
        price_brank = jd['manufacturer']['en']
        pb_list.append(c_number)
        inventory = jd['stock']
        if int(inventory) > 0:

            redis_data.hmset(price_brank, {"%s" % c_number: "%s" % jd})
        else:
            pass
            redis_no_data.hmset(price_brank, {"%s" % c_number: "%s" % jd})


if __name__ == '__main__':

    endnumber = page_url()
    print(f"目前网页一共{endnumber}页数据")
    Incremental_crawler = False # 修改成 True, 就是增量爬虫

    if Incremental_crawler==True:
        page_number_list = []
        with open('page.txt','r') as f:
            number = str(f.read()).split('\n')
            for num in number:
                if num != "":
                    page_number_list.append(int(num))

        notupdated_number = max(page_number_list)
        for x in range(int(notupdated_number), int(endnumber)+1):
            data = {
                "current_page": "%s" % x,
                "category": "365",
                "in_stock": "false",
                "is_RoHS": "false",
                "show_icon": "false",
                "search_content": "",
                "limit": "25"
            }
            Form_data_list.append(data)

        ri_list = []
        for i in range(5):
            rjd = threading.Thread(target=requests_info)
            ri_list.append(rjd)
            # rjd.start()
        for rl in ri_list:
            rl.start()
        for rl in ri_list:
            rl.join()

    else:
        # 全量爬虫
        for x in range(1, int(endnumber)+1):
            data = {
                "current_page": "%s" % x,
                "category": "365",
                "in_stock": "false",
                "is_RoHS": "false",
                "show_icon": "false",
                "search_content": "",
                "limit": "25"
            }
            Form_data_list.append(data)

        ri_list = []
        for i in range(5):
            rjd = threading.Thread(target=requests_info)
            ri_list.append(rjd)
            # rjd.start()
        for rl in ri_list:
            rl.start()
        for rl in ri_list:
            rl.join()
