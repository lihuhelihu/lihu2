
# encoding:utf-8

import requests
import base64

'''
通用文字识别（高精度版）
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
import os
path=r'E:\PycharmProjects\OCR识别图片表格\图片输入文件夹'
file_path=os.listdir(path)
# print(file_path)
for i in file_path:
    file_paths=os.path.join(path,i)
    f = open(file_paths, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = '24.6de9916b7db86dab45180e23c9bc22ae.2592000.1688806644.282335-34554659'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        # print (response.json())
        jsons=response.json()
        words=jsons['words_result']
        print(words)