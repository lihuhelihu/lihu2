import os
from aip import AipOcr
import requests
import time
import tkinter as tk
from tkinter import filedialog

APP_ID='34497211'
API_KEY='Giea1weVrG4wpXbEOGSmchzX'
SECRET_KEY='GSz9m7V7NT8NGNzXcZYrciHzM0n2GTRm'

# 调用申请的应用
client=AipOcr(APP_ID,API_KEY,SECRET_KEY)
# 定义读取文件函数，返回读取文件
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

# 文件下载函数
def file_download(url,file_path):
    r=requests.get(url)
    with open(file_path,'wb') as f:
        # print(r.content)
        f.write(r.content)

# 定义图片的输入输出文件夹的路径
root=tk.Tk()
root.withdraw()

# 输入文件夹
# data_dir=filedialog.askdirectory(title='请选择图片文件夹')+'/'
data_dir=r'E:\PycharmProjects\OCR识别图片表格\图片输入文件夹'
print('data_dir'*50)
print(data_dir)
# 输出文件的文件夹
# result_dir=filedialog.askdirectory(title='请选择输出文件的文件夹')+'/'
result_dir=r'E:\PycharmProjects\OCR识别图片表格\图片导出文件夹'

num=0
for name in os.listdir(data_dir):
    print('name'*50)
    print(name)
    print("name===",name)
    image=get_file_content(os.path.join(data_dir,name))
    print('image'*50)
    print(image)
    # 调研表格文字识别应用
    res=client.tableRecognitionAsync(image)
    print("res===",res)
    # 获取识别ID
    req_id=res['result'][0]['request_id']
    print(req_id)
    for count in range(1,10):
        res=client.getTableRecognitionResult(req_id)
        print('res'*10)
        print(res)
        print('res' * 10)
        print(res['result']['ret_msg'])
        if res['result']['ret_msg']=='已完成':
            break
        else:
            time.sleep(1)
    url=res['result']['result_data']
    xls_name=name.split('.')[0]+'.xls'
    file_download(url,os.path.join(result_dir,xls_name))
    num=num+1
    print('{0}:{1}已经下载完成'.format(num,xls_name))
    time.sleep(1)