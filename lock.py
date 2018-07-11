import requests
import linecache
import random
import time
import datetime
from lxml import etree
import re

id = input("请输入锁定id：")
delay = 1
starttime = datetime.datetime.now()
vote_time = datetime.datetime.now()
piaoshu = 0
down_count = 0
down_time = ""
vote_count = 0
weigui_count = 0

count=0
thefile=open("lock.txt")
while True:
    buffer=thefile.read(1024*8192)
    if not buffer:
        break
    count+=buffer.count('\n')
thefile.close()

vote_url = "http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&id=%s&do=vote&m=tyzm_diamondvote" %id
real_url = "http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&id=%s&do=view&m=tyzm_diamondvote" %id
useragent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 wxwork/2.1.5 MicroMessenger/6.3.22'
cookie = "PHPSESSID=2773c81c10766cb0b977be50b585cb39; Hm_lpvt_2773c81c10766cb0b977be50b585cb39=1528786299; Hm_lvt_2773c81c10766cb0b977be50b585cb39=1528517742,1528726549,1528731505,1528765187"

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
for xxx in range(9999999):
    for a in range(99999):
        x = a % (count+1)
        theline = linecache.getline(r'lock.txt', x+1)  # 从代理ip池中按序挑选一个
        theline = r"http://" + theline[:len(theline) - 1]
        proxies = {"http": theline, "https": "https://127.0.0.1:3128"}
        try:
            response_real = requests.get(real_url, proxies=proxies,headers=real_headers, timeout=2)
            html1 = response_real.text
            page = etree.HTML(html1.lower())
            piaoshu1 = int(page.xpath("/html/body/div[1]/div[5]/div[2]/span[2]")[0].text)
            giftcount1 = re.sub("\D", "", page.xpath("/html/body/div[1]/div[5]/div[4]/span[2]")[0].text)
            print("%s第%d轮第一次检测票数为%d，礼物积分为%s，当前时间为%s"%(id,xxx+1,piaoshu1,giftcount1,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            time.sleep(30)
            break
        except:
            continue
    for b in range(99999):
        x = b % (count+1)
        theline = linecache.getline(r'lock.txt', x+1)  # 从代理ip池中按序挑选一个
        theline = r"http://" + theline[:len(theline) - 1]
        proxies = {"http": theline, "https": "https://127.0.0.1:3128"}
        try:
            response_real = requests.get(real_url, proxies=proxies,headers=real_headers, timeout=2)
            html1 = response_real.text
            page = etree.HTML(html1.lower())
            piaoshu2 = int(page.xpath("/html/body/div[1]/div[5]/div[2]/span[2]")[0].text)
            giftcount2 = re.sub("\D", "", page.xpath("/html/body/div[1]/div[5]/div[4]/span[2]")[0].text)
            print("%s第%d轮第二次检测票数为%d，礼物积分为%s，当前时间为%s"%(id,xxx+1,piaoshu2,giftcount2,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            break
        except:
            continue

    if ((piaoshu2 - piaoshu1 > 0) and (int(giftcount2) - int(giftcount1) < 1)):
        weigui_count+=1
        print("违规%d次"%weigui_count)
    else:
        weigui_count=0
        print("解除违规")
        continue
    if(vote_count>30):
        print("lock池太弱")
        break
    if(weigui_count>2):
        count = 0
        thefile = open("lock.txt")     #注意！！！！！！！！lock.txt末尾不能用空行
        while True:
            buffer = thefile.read(1024 * 8192)
            if not buffer:
                break
            count += buffer.count('\n')
        thefile.close()
        linecache.clearcache()
        for c in range(9999999):  # 无限循环
            x = c % (count+1)
            theline = linecache.getline(r'lock.txt', x+1)  # 从代理ip池中按序挑选一个
            theline = r"http://" + theline[:len(theline) - 1]
            proxies = {"http": theline, "https": "https://127.0.0.1:3128"}
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
                'Referer': 'http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&id=%s&rid=14&do=view&m=tyzm_diamondvote' % id,
                'Content-Length': '31',
                'Cookie': cookie
            }
            try:
                response_vote = requests.post(vote_url, proxies=proxies, headers=vote_headers,data=" ", timeout=2)  # 模拟投票
                html2 = response_vote.text
                code = html2.split(",")[0].split(":")[1][1:2]  # 获取返回码，成功为1，失败为0
                print(theline)
            except:
                continue
            else:
                if (code == "1"):
                    vote_count += 1
                    print("%s投票成功！一共投了%s票" % (id, vote_count))
                    continue
                else:
                    try:
                        str = html2.split(":")[2].split("\"")[1]
                        if ("锁定" in str.encode('utf-8').decode('unicode_escape')):
                            print("%s刷票已被锁定，当前时间为%s，!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                            vote_count=0
                            weigui_count=0
                            break
                        else:
                            continue
                    except:
                        print("投票失败！")
                        continue
