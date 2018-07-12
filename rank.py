#!/usr/bin/env python
#-*- coding:utf-8 -*-
#AUTHOR:strongerz
#DESCRIBE:访问投票网站的排名页面，获取名次、票数、礼物等相关字段，整理后输出
#DATE:2018-7-12

import re
import requests
import linecache
import random
import time
import datetime
from lxml import etree

rank_url = "http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&do=ranking&m=tyzm_diamondvote"
rank_headers = {
    'Host': '101.chinalife-pension.com.cn',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Proxy-Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://101.chinalife-pension.com.cn',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 MicroMessenger/6.7.0 NetType/WIFI Language/zh_CN',
    'Connection': 'keep-alive',
    'Referer': 'http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&do=ranking&m=tyzm_diamondvote&u=126263&wxref=mp.weixin.qq.com',
    'Content-Length': '7',
    'Cookie': 'PHPSESSID=a52be5a3095b3ddb29c88c4a4e88b24d; Hm_lpvt_08c6f5e17c0761a968c5658ccf6ff5ad=1531046739; Hm_lvt_08c6f5e17c0761a968c5658ccf6ff5ad=1530972177,1531005903,1531008783,1531045193'
}
id = []
giftcount1 = ['6890','1984','6972','5738','1370','5225','4251','3936','3','1218']    #前十名的起始礼物数，用于计算增幅，可以修改
giftcount2 = []                                                                      #前十名的当前礼物数，用于计算增幅，不可修改
votecount1 = ['38441', '38292', '36943', '30071', '26291', '25451', '23626', '23081', '21340', '21228']#前十名的起始票数，用于计算增幅，可以修改
votecount2 = []                                                                                        #前十名的当前票数，用于计算增幅，不可修改

#无限循环地获取、整理、输出排名情况
for a in range(999999):
    #尝试获取排名数据
    try:
        response_rank = requests.post(rank_url, headers=rank_headers, data="limit=1", timeout=2)
        html = response_rank.text
        print("==========================%s==========================" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    except:
        continue
    #循环整理前十名的数据
    for i in range(10):
        id.append(html.split("\"id\"")[i+1].split("\"")[1])
        votecount2.append(html.split("\"id\"")[i+1].split("\"votenum\"")[1].split("\"")[1])
        giftcount2.append(html.split("\"id\"")[i+1].split("\"giftcount\"")[1].split(",")[0].split(":")[1])
    #循环输出前十名的数据
    for k in range(10):
        print("第%d名ID为%s，票数%s，礼物%s，票数增幅%d，礼物增幅%d" % (k+1, id[k], votecount2[k],giftcount2[k],int(votecount2[k])-int(votecount1[k]),int(giftcount2[k])-int(giftcount1[k])))
    #将当前礼物数和票数 赋值给 起始礼物数和票数，用于进行下一次的计算
    votecount1=votecount2
    giftcount1=giftcount2
    #将id，当前礼物数和票数进行初始化，防止append函数再一次循环导致列表长度溢出
    id = []
    votecount2 = []
    giftcount2 = []
    #每300秒输出一次数据
    time.sleep(300)




