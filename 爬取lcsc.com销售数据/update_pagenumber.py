#encoding:utf-8

def update_page(pages):
    with open('page.txt','a+',encoding='utf-8') as f:
        f.write(pages+'\n')
        f.close()
