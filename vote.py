#!/usr/bin/env python
#-*- coding:utf-8 -*-
#AUTHOR:strongerz
#DESCRIBE:仿造投票请求进行刷票。需要将代理IP放在vote.txt中
#DATE:2018-7-12

import requests
import linecache
import random
import time
import datetime
from lxml import etree

#随机生成sessionID
def getsessionid():
    list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    str = ""
    for i in range(32):
        a = random.randrange(0, 16)
        str = str + "".join(list[a])
    return (str)


id = input("请输入投票id：")
delay = int(input("请输入投票间隔(推荐29秒)："))
print("=====系统正在初始化，%d秒后自动开始====="%delay)
starttime = datetime.datetime.now()
vote_time = datetime.datetime.now()
time.sleep(delay)

piaoshu = 0       #表示当前票数
down_count = 0    #刷票被发现时的异常票数
down_time = ""    #刷票被发现时的异常时间
vote_count = 0    #表示刷了几票

#计算代理IP的数量，count+1才是代理IP的实际数量
count=0
thefile=open("vote.txt")
while True:
    buffer=thefile.read(1024*8192)
    if not buffer:
        break
    count+=buffer.count('\n')
thefile.close()

#以下为请求的URL，view表示打开投票界面的URL，count表示服务器用于计数的URL，vote表示投票URL，real用于检测实时票数跟view功能差不多
view_url = "http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&id=%s&do=view&m=tyzm_diamondvote" %id
count_url = "http://100.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&id=%s&do=Count&m=tyzm_diamondvote" %id
vote_url = "http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&id=%s&do=vote&m=tyzm_diamondvote" %id
real_url = "http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&id=%s&do=view&m=tyzm_diamondvote" %id

#以下useragent待选
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en",\
      "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/6.5.17 NetType/WIFI Language/zh_HK",\
      "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.16 NetType/WIFI Language/zh_CN",\
      "Mozilla/5.0 (Linux; Android 6.0; MX6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",\
      "Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13A405 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN",\
      "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",\
      "Mozilla/5.0 (Linux; Android 7.0; VTR-AL00 Build/HUAWEIVTR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 wxwork/2.1.3 MicroMessenger/6.3.22",\
      "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 wxwork/2.1.3 MicroMessenger/6.3.22",\
      "Mozilla/5.0 (Linux; Android 5.1; m3 note Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 wxwork/2.1.3 MicroMessenger/6.3.22",\
      "Mozilla/5.0 (Linux; Android 6.0; MX6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 wxwork/2.1.3 MicroMessenger/6.3.22",\
      "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 wxwork/2.1.5 MicroMessenger/6.3.22",\
      "Mozilla/5.0 (Linux; Android 7.0; EVA-AL00 Build/HUAWEIEVA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",\
      "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A402 MicroMessenger/6.5.16 NetType/WIFI Language/zh_CN",\
      "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",\
      "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",\
      "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",\
      "Mozilla/5.0 (Linux; Android 7.0; WAS-AL00 Build/HUAWEIWAS-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN"]

#无限循环进行刷票
for a in range(9999999):
    count = 0
    thefile = open("vote.txt")    #注意！！！！！！！！vote.txt末尾不能用空行
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count('\n')
    thefile.close()
    linecache.clearcache()

    #获取代理IP、sessionID、UserAgent、Header
    x = a%(count+1)
    theline = linecache.getline(r'vote.txt', x+1)       #从代理ip池中按序挑选一个
    theline = r"http://" + theline[:len(theline)-1]      #将代理整理为http://xx.xx.xx.xx的格式
    randomc = getsessionid()                             #随机生成session id
    proxies = { "http": theline,"https": "https://127.0.0.1:3128"}
    cookie = "PHPSESSID=" + randomc + "; Hm_lpvt_" + randomc + "=1528786299; Hm_lvt_" + randomc + "=1528517742,1528726549,1528731505,1528765187"
    useragent = ua[random.choice(range(16))]
    view_headers = {
        'Host': '101.chinalife-pension.com.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://101.chinalife-pension.com.cn',
        'Proxy-Connection': 'keep-alive',
        'Accept-Language': 'zh-cn',
        'Referer': 'http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&id=%s&do=view&m=tyzm_diamondvote&wxref=mp.weixin.qq.com'%id,
        'Accept-Encoding': 'gzip, deflate',
        'Content-Length': '7',
        'User-Agent': useragent,
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cookie
    }
    count_headers = {
        'Host': '101.chinalife-pension.com.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Proxy-Connection': 'keep-alive',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': useragent,
        'Referer': 'http://100.chinalife-pension.com.cn/app/index.php?i=2&c=entry&id=%s&rid=14&do=view&m=tyzm_diamondvote'%id,
        'Connection': 'keep-alive',
        'Cookie': cookie
    }
    vote_headers = {
        'Host': '101.chinalife-pension.com.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Proxy-Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://101.chinalife-pension.com.cn',
        'User-Agent': useragent,
        'Connection': 'keep-alive',
        'Referer': 'http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&id=%s&rid=14&do=view&m=tyzm_diamondvote'%id,
        'Content-Length': '31',
        'Cookie': cookie
    }
    real_headers = {
        'Host': '101.chinalife-pension.com.cn',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': 'Hm_lpvt_08c6f5e17c0761a968c5658ccf6ff5ad=1530891725; Hm_lvt_08c6f5e17c0761a968c5658ccf6ff5ad=1530789720,1530833997,1530853117,1530891687; PHPSESSID=60a8ce8ccc41a2c988f84901ad457c2c',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 MicroMessenger/6.7.0 NetType/WIFI Language/zh_CN',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }

    #开始进行投票
    try:
        response_view = requests.post(view_url, proxies=proxies,headers=view_headers,data="limit=1",timeout = 2)   #模拟打开页面
        response_real = requests.get(real_url, proxies=proxies,headers=real_headers, timeout=2)
        response_count = requests.get(count_url, proxies=proxies,headers=count_headers ,timeout = 2)    #模拟打开统计页面
        response_vote = requests.post(vote_url, proxies=proxies, headers=vote_headers, data="latitude=0&longitude=0&verify=0",timeout = 2)   #模拟投票
        html2 = response_vote.text
        code = html2.split(",")[0].split(":")[1][1:2]  # 获取返回码，成功为1，失败为0
        print(theline)
    except:
        continue
    else:
        #如果服务器返回码为1，表示投票成功
        if (code == "1"):
            try:
                #将服务器返回的数据进行格式化整理，以便后续提取
                html1 = response_real.text
                page = etree.HTML(html1.lower())
                #如果出现票数减少的异常情况，记录下时间和减少的数量
                if (int(page.xpath("/html/body/div[1]/div[5]/div[2]/span[2]")[0].text)) < piaoshu:
                    down_time = datetime.datetime.now()      #出现异常的时间
                    down_count = piaoshu - int(page.xpath("/html/body/div[1]/div[5]/div[2]/span[2]")[0].text)   #出现异常的票数
                #获取当前的票数
                piaoshu = int(page.xpath("/html/body/div[1]/div[5]/div[2]/span[2]")[0].text)
                #总刷票数加1
                vote_count += 1
                print("%s投票成功！一共投了%s票，当前票数为%s，距上次投票为%s秒，%s秒后再投" % (id,vote_count,piaoshu,(datetime.datetime.now() - vote_time).seconds,delay))
                print("程序启动时间为%s,当前时间为%s" %(starttime.strftime('%Y-%m-%d %H:%M:%S'),datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                #一旦出现票数减少的异常情况，进行报警
                if (down_count != 0):
                    print("异常时间为%s，异常票数为%d!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (down_time, down_count))
                    down_count=0
                #记录下投票的时间
                vote_time = datetime.datetime.now()
                #投票成功后，需要延迟一会再投，防止被封锁
                time.sleep(delay)
                continue
            except:
                vote_count += 1
                print("%s投票成功！一共投了%s票，但无法读取当前票数，距上次投票为%s秒，%s秒后再投" % (id, vote_count, (datetime.datetime.now() - vote_time).seconds, delay))
                print("程序启动时间为%s,当前时间为%s" %(starttime.strftime('%Y-%m-%d %H:%M:%S'),datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                vote_time = datetime.datetime.now()
                time.sleep(delay)
                continue
        #如果服务器返回码为0，表示投票失败
        else:
            #输出投票失败，并尝试输出投票失败的原因
            try:
                str = html2.split(":")[2].split("\"")[1]
                print("投票失败！%s" % str.encode('utf-8').decode('unicode_escape'))
                continue
            except:
                print("投票失败！")
                continue