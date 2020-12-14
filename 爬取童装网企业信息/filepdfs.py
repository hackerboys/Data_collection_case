#encoding:utf-8
"""
自己写的转pdf

"""

import pdfkit

def pdf_htmlfile(fileName,htmlpath,savepath):
    confg = pdfkit.configuration(wkhtmltopdf=r"D:\pro_py\wkhtmltopdf\bin\wkhtmltopdf.exe") # 自行到网上下载wkhtmltopdf.exe，并设置这里的路径
    pdfkit.from_file(htmlpath, '%s/%s.pdf' % (savepath,fileName), configuration=confg)
    print(fileName + "转换成功")

def pdf_weburl(fileName,weburl,savepath):
    confg = pdfkit.configuration(wkhtmltopdf=r"D:\pro_py\wkhtmltopdf\bin\wkhtmltopdf.exe") #自行到网上下载wkhtmltopdf.exe，并设置这里的路径
    pdfkit.from_file(weburl, '%s/%s.pdf' % (savepath,fileName), configuration=confg)
    print(fileName + "转换成功")

def pdf_string(fileName,strings,savepath):
    confg = pdfkit.configuration(wkhtmltopdf=r"D:\pro_py\wkhtmltopdf\bin\wkhtmltopdf.exe") #自行到网上下载wkhtmltopdf.exe，并设置这里的路径
    pdfkit.from_file(strings, '%s/%s.pdf' % (savepath,fileName), configuration=confg,)
    print(fileName + "转换成功")


if __name__ == '__main__':
    # htmlfile("name","http://www.61ef.cn/brand/list-15-0-0-0-0-1.html","D:/")
    pass
