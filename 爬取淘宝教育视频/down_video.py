#encoding:utf-8
"""
功能：根据  py的保存路径下载视频

"""

import os
import requests
path = 'pro_file'



filepath = os.listdir(path)
for f in filepath:

    class_name = f # 分类文件名称
    filepath2 = os.path.join(path,f) # 分类路径
    print(filepath2)
    filepath3 = os.listdir(filepath2)
    for f3 in filepath3:

        filename = str(f3).replace('.txt','') # 视频文件名称
        video_path = os.path.join(filepath2,f3)
        with open(video_path,'r',encoding='utf-8') as f:
            down_url = f.read()
            requ = requests.get(down_url)
            with open("%s/%s.mp4"%(filepath2,filename),'wb') as m:
                m.write(requ.content)
                m.close()

