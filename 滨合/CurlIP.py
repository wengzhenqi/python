import requests,re
from requests.auth import HTTPBasicAuth
from lxml import etree
EnterInput = input("""pealse select
---------------------
|1.goodworkers       |
---------------------
|2.goodworkers4      |
---------------------
|3.wrongworkers      |
---------------------
|4.offlineworkers    |
---------------------
|5.delOfflineWorker  |
---------------------
|6.delOfflineWorker  |
---------------------
|7.unknowworkers     |
---------------------
请输入:""")
#获取页面li数据列表
def GetHtmlIp(COUNT):
    count = int(COUNT)
    auth = HTTPBasicAuth("yzq".encode('utf-8'), "111.")
    resopnse = requests.get("https://bweb.wutoon.com/status", auth=auth)
    html = etree.HTML(resopnse.text)
    name = html.xpath('//div[@class="box"]/dl[{}]/dd/li'.format(int(count)))
    for i in name:
        if count == 2:
            print(str(i.text).split(",")[0])
        if count == 4:
            if str(i.text).split(" ")[0].split("-")[0]:
                ErrorOut = str(i.text).split(" ")
                if 'no' in ErrorOut and 'host':
                    print(ErrorOut[0])
        elif str(i.text).split(" ")[0].split("-")[0]:
            print(str(i.text).split(" ")[0].split("-")[1])
if __name__ == '__main__':
    GetHtmlIp(EnterInput)

