#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/19 10:47
# @Author : fengmiao
# @File : test.py


import requests
url='http://gdj.beijing.gov.cn/xzxkxxgsNEW/xzxkxxgsgl.html'
url_tmp = url.split("/")
url_change= "http://"+url_tmp[2]+"/"+url_tmp[3]+"/"
head = {}
#写入User Agent信息
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
#创建Request对象
#req = request.Request(url, headers=head)
#传入创建好的Request对象
#response = request.urlopen(req)
strhtml=requests.get(url, headers=head)
# 读取响应信息并解码
#html = response.read().decode('utf-8')

from bs4 import BeautifulSoup
soup=BeautifulSoup(strhtml.text,'lxml')
data=soup.select('body > div.topbg > div.box > div.hyjj_part1 > ul > li > span.txt > a')

import re
for item in data:
    item_url_tmp = item.get('href').split("/")
    item_url = url_change+item_url_tmp[1]+"/"+item_url_tmp[2]
    strhtmlcontext = requests.get(item_url, headers=head)
    soup_context=BeautifulSoup(strhtmlcontext.text,'lxml')
    data_context=soup_context.select('body > div > div.box > div.detail > div.detail_con > table > tr > td.nr')
    for item_detail in data_context:
        result={
            "context":item_detail.get_text()
        }
        print(result)

# 打印信息
