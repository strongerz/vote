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
giftcount1 = ['1948','5840','5972','5738','1360','5225','4251','3936','1218','3']
giftcount2 = []
votecount1 = ['37931', '33340', '32215', '29514', '26238', '25449', '23626', '23081', '21193', '19192']
votecount2 = []
for a in range(999999):
    try:
        response_rank = requests.post(rank_url, headers=rank_headers, data="limit=1", timeout=2)  # 模拟投票
        html = response_rank.text
        print("==========================%s==========================" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    except:
        continue
    for i in range(1, 11):
        id.append(html.split("\"id\"")[i].split("\"")[1])
        votecount2.append(html.split("\"id\"")[i].split("\"votenum\"")[1].split("\"")[1])
        giftcount2.append(html.split("\"id\"")[i].split("\"giftcount\"")[1].split(",")[0].split(":")[1])
    for k in range(10):
        print("第%d名ID为%s，票数%s，礼物%s，票数增幅%d，礼物增幅%d" % (k+1, id[k], votecount2[k],giftcount2[k],int(votecount2[k])-int(votecount1[k]),int(giftcount2[k])-int(giftcount1[k])))
    votecount1=votecount2
    giftcount1=giftcount2
    id = []
    votecount2 = []
    giftcount2 = []
    time.sleep(3600)




