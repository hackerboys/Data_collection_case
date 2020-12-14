#encoding:utf-8
"""
作者：宋哈哈
代码功能：
    解压所有的PPT

使用说明：
    注意路径设置

"""


import zipfile
import os
import shutil
from del_ppt_logopage import pptxde # 导入自定的包，请设置环境变量。在Pycharm - 右键py所在的文件夹-Mack Drectory as - Sources Root
from pptx import Presentation

def unzipfiles():
    filepath = "pptzipfile"
    newfilepath = "unzip"
    filename = os.listdir(filepath)
    for f in filename:
        file_folder = os.path.join(filepath,f) # 分类文件夹
        new_file_folder = os.path.join(newfilepath,f)
        ppt = os.listdir(file_folder)
        for p in ppt:
            ppt_filepath = os.path.join(file_folder,p)
            new_ppt_filepath = os.path.join(new_file_folder,p)
            unzip(ppt_filepath,new_ppt_filepath,file_folder)

def unzip(ppt_filepath,new_ppt_filepath,save_path):

    try:
        zf = zipfile.ZipFile(r"%s"%ppt_filepath,'r')
        for z in zf.namelist():
            zf.extract(z,r'%s'%save_path)
    except:
        shutil.move(ppt_filepath,new_ppt_filepath)
    else:
        pass

def moveppt():
    endfilepath = "endppt"
    filepath = "unzip"
    filename = os.listdir(filepath)
    for f in filename:
        file_folder = os.path.join(filepath, f)  # 分类文件夹
        end_file_folder = os.path.join(endfilepath, f)
        ppt = os.listdir(file_folder)
        for p in ppt:
            ppt_filepath = os.path.join(file_folder, p)
            end_filepath = os.path.join(end_file_folder, p)
            class_file = str(ppt_filepath).split('.')
            try:
                if str(class_file[1]) == "pptx" :
                    print(ppt_filepath,end_filepath)
                    shutil.move(ppt_filepath,end_filepath)

                elif str(class_file[1]) == "ppt":
                    shutil.move(ppt_filepath, end_filepath)

            except:
                pass

def del_ppt():
    global ppt_filepath
    endfilepath = "endppt"
    delfilepath = "def_ppt"
    filename = os.listdir(endfilepath)
    for f in filename:
        file_folder = os.path.join(endfilepath, f)  # 分类文件夹
        del_file_folder = os.path.join(delfilepath, f)
        ppt = os.listdir(file_folder)
        for p in ppt:
            try:
                ppt_filepath = os.path.join(file_folder, p)
                del_filepath = os.path.join(del_file_folder, p)
                pptxde(ppt_filepath, del_filepath)
            except:
                print("%s"%ppt_filepath+"删除失败")
                pass


def pptnum():
    delfilepath = "def_ppt"
    filename = os.listdir(delfilepath)
    pptlist = []
    for f in filename:
        ppt_path = os.path.join(delfilepath,f)

        file_name_ppt = os.listdir(ppt_path)
        for fn in file_name_ppt:
            # print(fn)
            pptlist.append(fn)

    print(len(pptlist))



if __name__ == '__main__':
    #
    pptnum()
