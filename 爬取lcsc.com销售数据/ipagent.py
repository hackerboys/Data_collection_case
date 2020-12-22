import json
import requests

def agent():

    try:
        ipapi = "请更换你的代理IP的API"
        respon = requests.get(ipapi)

        ip_port = json.loads(respon.content)['data']['proxy_list'][0]
        return ip_port
    except:
        print("IP代理请求报错，关闭了现有连接")


if __name__ == '__main__':
    agent()
