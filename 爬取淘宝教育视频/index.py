# encoding:utf-8
"""
1.需要登录自己的淘宝账号
2.需要下载chromedriver，根据自己google版本下载对应版本。并在代码中更改路径。
3.url是 手机分享链接，在浏览器打开是竖屏模式。

"""
import json
import requests
from selenium import webdriver
import time
import os
headers = {
    # 'cookie':'cna=d9MyGFXJy3ECAd+VP+C9tMBO; _m_h5_tk=fd0dcb980c4bb8d4bb200b65848c0b0b_1605111359929; _m_h5_tk_enc=64fc55729b0678e8f4e1ce878a9e413f; cookie2=1677f4a1a649100c194e4729930edfd2; t=29bbbfdee40cdae4ef00175b0b6b0d52; _tb_token_=e1e795083e031; _samesite_flag_=true; xlly_s=1; tfstk=cJSPBWc-yuEPCztQW3tEPjmCRSLRZMXlKmJ6rwoA77GUw3TliXlpn8bM3pOTmUf..; ockeqeudmj=mravPk0%3D; _w_tb_nick=%E7%8B%82%E9%A3%99%E7%9A%84%E8%9C%97%E7%89%9Bye; munb=2701589139; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2Bu50IDqlWEadoeeFOG9NuUXcUIw%3D%3D; _w_app_lg=0; sgcookie=E10099yD1YiYYjAQLQzVKLKIWUsl%2BTK2xxRgIhtnb5XRWE448Ao8gy3h6IkuaLit2SQNJlCfhdqvSuvbmlooKijo2A%3D%3D; unb=2701589139; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dCufOCQdmQJL524GE%3D&nk2=3EWY2QbTAkdb7KWx&id2=UU8IPTyRbKU2yw%3D%3D; uc1=cookie14=Uoe0aD3LMu58Zw%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie21=WqG3DMC9Edo1SB5NB6Qtng%3D%3D&existShop=true; csg=2a4a3f56; lgc=%5Cu72C2%5Cu98D9%5Cu7684%5Cu8717%5Cu725Bye; ntm=0; cookie17=UU8IPTyRbKU2yw%3D%3D; dnk=%5Cu72C2%5Cu98D9%5Cu7684%5Cu8717%5Cu725Bye; skt=cb1d6520a45792bb; uc4=nk4=0%403jG%2Fc5Qu3r%2B0Ew2RwiFRlxgVGjEiX24%3D&id4=0%40U22PGMm3NWDuPibXLvJw2b42sdl9; tracknick=%5Cu72C2%5Cu98D9%5Cu7684%5Cu8717%5Cu725Bye; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; sg=e90; _nk_=%5Cu72C2%5Cu98D9%5Cu7684%5Cu8717%5Cu725Bye; cookie1=B0EzweA7TLKhu4P1CHazoo1aUxo3HEXdG9jckoF2hK4%3D; isg=AmRk0H2M53wdMBOwyVXRSt-QNWIPTpen9sLlnn6F6i_yKQTzpg1Y95qPnzfN; l=AomJ4AWMVtIQxi0vYpuqC/gDGb7jzH0I',

    'cookie':'cna=BzcpGD+dYjUCAd+VQzVfH0gp; lgc=%5Cu72C2%5Cu98D9%5Cu7684%5Cu8717%5Cu725Bye; tracknick=%5Cu72C2%5Cu98D9%5Cu7684%5Cu8717%5Cu725Bye; thw=cn; enc=i9M1y3B%2F9lEte6JjPplqFT68R%2FkEyR3tnIr%2BI1gZZ9hgTcv%2BHJpF1XCgJr04vNohDo9bbNGDaJPZOQmvrRIDcQ%3D%3D; t=07a4276138be8389e3560e2f0ba12ae0; miid=2055164070163868920; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; _fbp=fb.1.1604983772781.845569496; hng=CN%7Czh-CN%7CCNY%7C156; _w_tb_nick=%E7%8B%82%E9%A3%99%E7%9A%84%E8%9C%97%E7%89%9Bye; munb=2701589139; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2Bu50IDqlWEadoeeFOG9NuUXcUIw%3D%3D; _w_app_lg=0; xlly_s=1; sgcookie=E100lUndR9DLvGBW74N4aRThUBwdhIyrIEj1MTQH4a9E3qcijL3UoP4r7sccnc7ClfyiUSpzaAVSbhk%2FXFcF8vBwHw%3D%3D; uc3=id2=UU8IPTyRbKU2yw%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&nk2=3EWY2QbTAkdb7KWx&vt3=F8dCufOMOXW9b1BqWgM%3D; uc4=nk4=0%403jG%2Fc5Qu3r%2B0Ew2RwiFRlxgWZyB%2FbFc%3D&id4=0%40U22PGMm3NWDuPibXLvJw2pfVfuuC; _cc_=VFC%2FuZ9ajQ%3D%3D; mt=ci=37_1; tfstk=c7i5BpGwm_f57CLF4Y94UEhkREZha65bLUwKF4EQ05AMSnH4MsXAb5w-42fGDPef.; _m_h5_tk=b9d23539f1cbc8b8a1a9f3d352375cf0_1605283946106; _m_h5_tk_enc=21d03b9ac4eee3ca96c6ced27af25fe8; cookie2=22c7b2fe75abc02d076df67203b20e01; _tb_token_=79b4f1eb55abb; isg=AsHBP0cber5BV5aKHYKj1mlG0A2CXWpRANwzrSMWqUgnCuHcaz5FsO8Mmsiw; l=Am5usdtQzP1WE8mDIv7Vz9KuPs8wezJp',


    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",

    'host': 'api.m.taobao.com',

}

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
# chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option("useAutomationExtension", False)
# chrome_options.add_argument('--host-resolver-rules=MAP g.alicdn.com 127.0.0.1')

driver = webdriver.Chrome(r"D:\pro_py\auto_office\chromedriver\chromedriver.exe", chrome_options=chrome_options)
chrome_options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36')
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""", })
fahuo_login_url = "https://h5.m.taobao.com/xue/detail.htm?ut_sk=1.WrHJH%2BF63IwDAD7l4yx9ORsJ_21380790_1605021159729.Copy.10000&itemId=552400591967&sourceType=other&ttid=201200%40taobao_iphone_8.8.0&suid=E0B7CB1C-710F-4610-95F7-2F047A369759&un=f249ba94edcb21f83911dc70f8aca8ac&share_crt_v=1&spm=a2159r.13376460.0.0&sp_tk=cmhpN2NQbXJPS0Q=&cpp=1&shareurl=true&short_name=h.43dpkg8&bxsign=scd59xbtg7Htg78I-yuxEtr95S91S-KaaGvXhZeF38L2SpC7Snd8C30bU-b2Q3xUk745Jc2fKHdj9pF3C9ORG909CyQkA8WaRT-rsnCKw-LmV0&sm=ab441c&app=chrome"

driver.maximize_window()
driver.get(fahuo_login_url)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="J_BottomBanner"]/ul/li[4]/a').click()
time.sleep(2)
driver.find_element_by_css_selector('#fm-login-id').send_keys('***you username')
time.sleep(1)
driver.find_element_by_css_selector('#fm-login-password').send_keys('you password')
time.sleep(2)
driver.find_element_by_css_selector('#login-form > div.fm-btn > button').click()
time.sleep(10)

# url = 'https://api.m.taobao.com/h5/mtop.lifemallweb.courseinfomtopservice.getoutline/1.0/?appKey=12574478&t=1605036880894&sign=5c4fd7d263d2f5cdefa5d4dacc6adb2f&v=1.0&api=mtop.lifemallweb.courseinfomtopservice.getoutline&type=jsonp&dataType=jsonp&callback=mtopjsonp4&data=%7B%22courseId%22%3A%2278011%22%7D'
# url = 'https://api.m.taobao.com/h5/mtop.lifemallweb.courseinfomtopservice.getoutline/1.0/?appKey=12574478&t=1605076799899&sign=6144d16087af79182743b65fd887b3c7&v=1.0&api=mtop.lifemallweb.courseinfomtopservice.getoutline&type=jsonp&dataType=jsonp&callback=mtopjsonp4&data=%7B%22courseId%22%3A%2278011%22%7D'



# url = "https://api.m.taobao.com/h5/mtop.lifemallweb.courseinfomtopservice.getoutline/1.0/?appKey=12574478&t=1605101345112&sign=7aeb0c41b0bc943feb126a945606f499&v=1.0&api=mtop.lifemallweb.courseinfomtopservice.getoutline&type=jsonp&dataType=jsonp&callback=mtopjsonp4&data=%7B%22courseId%22%3A%2278011%22%7D"
url = 'https://api.m.taobao.com/h5/mtop.lifemallweb.courseinfomtopservice.getoutline/1.0/?appKey=12574478&t=1605275205588&sign=5b47cc8aafc78339c8535a48fbbca372&v=1.0&api=mtop.lifemallweb.courseinfomtopservice.getoutline&type=jsonp&dataType=jsonp&callback=mtopjsonp4&data=%7B%22courseId%22%3A%2278011%22%7D'


requ = requests.get(url, headers=headers)
html = requ.text.replace('mtopjsonp4(', '').replace(')', '')
jsontext = json.loads(html)
print(jsontext)
datas = jsontext['data']['data']['outline']['chapters']

# 'https://h5.m.taobao.com/xue/play/index.html?spm=a2174.7623065.6.4&resourceId= 5183000 &sectionId= 11093072 &channel=2&courseId= 78011 &resourceId= 5183000 &live=false&title=4 &resourceId= 5183000 &sectionId= 11093072 &channel=2&courseId= 78011 &resourceId= 5183000 &live=false&title='

number = 0
'https://h5.m.taobao.com/xue/play/index.html?spm=a2174.7623065.6.5&resourceId=5184940&sectionId=11064015&channel=2&courseId=78011&resourceId=5184940'
'https://h5.m.taobao.com/xue/play/index.html?spm=a2174.7623065.6.5&resourceId=5184940&sectionId=11064015&channel=2&courseId=78011&resourceId=5184940'
for d in datas:
    video_url_info = d['sections']
    courseid = d['courseId']
    zj_title = d['title']  # 章节
    print(zj_title)
    # print(courseid)
    for v in video_url_info:
        v_id = v['resources']
        sectionid = v['id']
        # print(sectionid)
        for vi in v_id:
            video_id = vi['id']
            video_title = vi['title']  # 文章标题
            print(video_title)
            # print(video_id)
            number += 1
            url = 'https://h5.m.taobao.com/xue/play/index.html?spm=a2174.7623065.6.%s&resourceId=%s&sectionId=%s&channel=2&courseId=%s&resourceId=%s' % (
            number + 3, video_id, sectionid, courseid, video_id)
            print(url)
            driver.get(url)
            down_url = driver.find_element_by_css_selector('#J_Video > source:nth-child(2)').get_attribute('src')
            time.sleep(5)
            driver.get(down_url)
            time.sleep(3)
            mp4_url = driver.current_url

            print(mp4_url)
            while True:
                if os.path.isdir("pro_file/%s"%zj_title):
                    with open("pro_file/%s/%s.txt"%(zj_title,video_title),'w',encoding='utf-8') as f:
                        f.write(mp4_url)
                        f.close()
                        break


                else:
                    os.makedirs("pro_file/%s"%zj_title)
