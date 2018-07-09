import requests
import linecache
import random
import time
import datetime
from lxml import etree
#import sys
#print(sys.path.append(requests))

def getsessionid():
    list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    str = ""
    for i in range(32):
        a = random.randrange(0, 16)
        str = str + "".join(list[a])
    return (str)
def getproxy_github():
    url = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"
    response = requests.get(url)
    html = response.text
    filename = 'origin.txt'
    with open(filename, 'w') as f:  
        f.write(html)
    f.close()

    count = 0
    thefile = open("origin.txt")
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count('\n')
    thefile.close()
    # print(count)

    filename = 'filtered.txt'
    with open(filename, 'w') as f:
        for i in range(1, count):
            theline = linecache.getline(r'origin.txt', i)
            a = theline.split("country")[1].split(',')[0][4:].split("\"")[0]
            b = theline.split("type")[1].split(',')[0][4:].split("\"")[0]
            if (a == "CN" and b == "http"):
                # print(theline)
                f.write(theline)
    f.close()

    count = 0
    thefile = open("filtered.txt")
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count('\n')
    thefile.close()

    filename = 'unknownalive.txt'
    with open(filename, 'w') as f:
        for x in range(1, count):
            theline = linecache.getline(r'filtered.txt', x)
            theline = theline.split("}")[0]
            theline = theline.split("host\"")[1][3:].split("\"")[0] + ":" + theline.split("port\"")[1][2:].split(",")[0] + "\n"
            f.write(theline)

    filename = 'alive.txt'
    url = "http://www.baidu.com"
    with open(filename, 'w') as f:
        for a in range(1, count):
            theline = linecache.getline(r'unknownalive.txt', a)
            theline1 = r"http://" + theline[:len(theline) - 1]
            proxies = {"http": theline1, "https": theline}
            try:
                response = requests.get(url, proxies=proxies, timeout=5)
            except:
                continue
            else:
                html = str(response)
                if (html == "<Response [200]>"):
                    print(theline)
                    f.write(theline)

id = input("请输入投票id：")
delay = int(input("请输入投票间隔(推荐29秒)："))
auto = input("是否需要自动获取代理(y/n)：")
print("=====系统正在初始化，%d秒后自动开始====="%delay)
starttime = datetime.datetime.now()
vote_time = datetime.datetime.now()
if (auto=="y"):
    getproxy_github()
time.sleep(delay)

piaoshu = 0
down_count = 0
down_time = ""

count=0
thefile=open("alive.txt")
while True:
    buffer=thefile.read(1024*8192)
    if not buffer:
        break
    count+=buffer.count('\n')
thefile.close()
#print(count)  #获取文件行数

view_url = "http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&id=%s&do=view&m=tyzm_diamondvote" %id
count_url = "http://100.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&id=%s&do=Count&m=tyzm_diamondvote" %id
vote_url = "http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&id=%s&do=vote&m=tyzm_diamondvote" %id
real_url = "http://101.chinalife-pension.com.cn/app/index.php?i=2&c=entry&rid=14&id=%s&do=view&m=tyzm_diamondvote" %id

vote_count = 0
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


for a in range(9999999):   #无限循环
    thefile = open("alive.txt")    #注意！！！！！！！！alive.txt末尾不能用空行
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count('\n')
    thefile.close()
    #x = random.randrange(1, count-1)
    #theline = linecache.getline(r'alive.txt', x)       #从代理ip池中随机挑选一个

    x = a%(count+1)
    theline = linecache.getline(r'alive.txt', x+1)       #从代理ip池中按序挑选一个

    theline = r"http://" + theline[:len(theline)-1]
    randomc = getsessionid()   #随机生成session id
#print(theline[:len(theline)-1])
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
        if (code == "1"):
            try:
                html1 = response_real.text
                page = etree.HTML(html1.lower())
                if (int(page.xpath("/html/body/div[1]/div[5]/div[2]/span[2]")[0].text)) < piaoshu:  # 如果出现票数减少的情况，记录下时间和减少的数量
                    down_time = datetime.datetime.now()
                    down_count = piaoshu - int(page.xpath("/html/body/div[1]/div[5]/div[2]/span[2]")[0].text)
                piaoshu = int(page.xpath("/html/body/div[1]/div[5]/div[2]/span[2]")[0].text)
                vote_count += 1
                print("%s投票成功！一共投了%s票，当前票数为%s，距上次投票为%s秒，%s秒后再投" % (id,vote_count,piaoshu,(datetime.datetime.now() - vote_time).seconds,delay))
                print("程序启动时间为%s,当前时间为%s" %(starttime.strftime('%Y-%m-%d %H:%M:%S'),datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                if (down_count != 0):  # 一旦出现票数减少的情况，进行循环提醒
                    print("异常时间为%s，异常票数为%d!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (down_time, down_count))
                    down_count=0
                vote_time = datetime.datetime.now()
                time.sleep(delay)
                continue
            except:
                vote_count += 1
                print("%s投票成功！一共投了%s票，但无法读取当前票数，距上次投票为%s秒，%s秒后再投" % (id, vote_count, (datetime.datetime.now() - vote_time).seconds, delay))
                print("程序启动时间为%s,当前时间为%s" %(starttime.strftime('%Y-%m-%d %H:%M:%S'),datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                vote_time = datetime.datetime.now()
                #print("%s无法读取当前票数！" % (datetime.datetime.now()))
                time.sleep(delay)
                continue
        else:
            try:
                str = html2.split(":")[2].split("\"")[1]
                print("投票失败！%s" % str.encode('utf-8').decode('unicode_escape'))
                continue
            except:
                print("投票失败！")
                continue