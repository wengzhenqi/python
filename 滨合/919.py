# '# for i in range(1,5)':'',
# '#     for j in range(1,5)':'',
# '#         for k in range(1,5)':'',
# '#             if ( i != k ) and (i != j) and (j != k)':'',
# #                 print (i,j,k)
#
#
# #斐波那契数
# '# def fib(n)':'',
# #     a,b = 1,1
# '#     for i in range(n - 1 )':'',
# #         a,b = b,a+b
# #     return a
# # a = fib(5)
# # print(a)
#
# #将一个列表的数据复制到另一个列表
# # a = [1,2,3]
# '# b = a[':']',
# # print(b)
#
# #乘法口诀表
# '# for i in range(1,10)':'',
# '#     for j in range(1,i+1)':'',
# #         print( "%s * %s = %s"%(i, j, i*j),end=' ' )
# #     print()
#
# #使用time模块的sleep（）函数
# # import time
# '# myD = {1':''a',2:'b'}',
# '# for key, value in dict.items(myD)':'       #item便利字典用的',
# #     print(key, value)
# #     time.sleep(1)
#
# #
# #暂停一秒输出，并格式化当前时间
# # import  time
# '# print (time.strftime('%Y-%m-%d %H':'%M:%S', time.localtime(time.time())))',
# # time.sleep(1)
# '# print (time.strftime('%Y-%m-%d %H':'%M:%S', time.localtime(time.time())))',
# '# while 1':'',
# #        time.sleep(1)
# '#        print (time.strftime('%Y-%m-%d %H':'%M:%S', time.localtime(time.time())))',
#
#
# #学习成绩，优秀，一般，差
# # number = int(input("请输入你的成绩： ").strip())
# '# if number >= 90':'',
# #     print("优秀")
# '# elif  number >= 60 and number <= 90':'',
# #     print("一般")
# '# else':'',
# #     print("好差")
#
#
#
#
# '# for n in range(2,10)':'',
# '#     for x in range(2,n)':'',
# '#         if n % x == 0':'',
# #             print(n,"equals",x,'*',n//x)
# '#     else':'',
# #         print(n,'is a prime numbber')
# #
# '# def fib(n)':'     #斐波那契数',
# #     a,b = 0,1
# '#     while a < n':'',
# #         print(a,end='  ')
# #         a,b = b, a+b
# #     print()
# #
# # fib(20000)
#
# #
# #
# # a = "my name is {name},age is {age}".format(name="egon",age=19)
# #
# # print(a)
#
# # 2020年10月27日
# '# a = input("my name is':' ")',
# '# b = input("my age is ':' ")',
# # res = f'my name is {a} and age is {b}'
# # print(res)
#
#
#
# #
# # a = "kks"
# # b = 22
# # res = f"my name is {a},and age is {b}"
# # print(res)
#
# # a = [111,222,333,444,555]
# # a1,a2,*_ = a
# # print(a1)
# # print(a2)
#
#
# # a = 10
# # b = 11
# # print(id(a))
# # print(id(b))
#
#
# # a = 10
# # b = 6
# # c = 1
# # print(a if a<b else 1)
#
# # a = 10
# # b = 7
# # c = a if a>b else b           如果条件满足输出左边结果，如果不满足输出右边
# # print(c)
#
#
#
#
#
# '# fp = open(r'D':'\mot.txt','a+')',
# # print("第三次测试",file=fp)          #输出到文件
# # fp.close()
#
# '# def fun_jisuan()':'           #三三之数余2，五五之数余3，七七之数余2，问？',
# '#     for x in range(1,1000)':'',
# '#         if x%3 == 2':'',
# '#             if x%5 == 3':'',
# '#                 if x%7 == 2':'',
# #                     print(x)
# # fun_jisuan()
# # 三三之数余2，五五之数余3，七七之数余2，问？
# '# for i in range(1,200)':'',
# '#         if i%3 == 2':'',
# '#             if i%5 == 3':'',
# '#                 if i%7 == 2':'',
# #                     print(i)
#
#
# # a = int(input("请输入您认为合适的数： ").strip())
# '# if a%3 == 2 and a%5 == 3 and a%7 == 2':'',
# #     print("恭喜您猜对了")
# '# else':'',
# #     print("您猜错了")
#
#
# # one = True
# # num = int(0)
# '# while one':'',
# #     num += 1
# '#     if num %3 == 2 and num%5 == 3 and num%7 ==2':'',
# #         print("这个数字是： ",num)
# #         one = False
#
#
# #计算1到100的计算累加
# # rest = 0
# '# for i in range(1,100)':'',
# #     rest += i
# # print(rest)
#
#
# # num = 0
# '# for i in range(0,101)':'              #注意：顾头不顾尾',
# #     num +=i
# # print(num)
#
#
# # 三三之数余2，五五之数余3，七七之数余2，问？
# '# def aa()':'',
# '#     while 1':'',
# '#         for i in range(100)':'',
# '#             if i%3 ==2 and i%5 == 3 and i%7 == 2':'',
# #                 print("这个数是： ",i)
# #         break
# #
# # aa()
#
# '# for i in range(100)':'',
# #     print(i)
# '#     if i%3 == 2 and i%5 == 3 and i%7 == 2':'',
# #         print("这个数是： ",i)
# #         continue
#
#
# # num = 0
# '# for i in range(100)':'',
# '#     if i %2 == 1':'',
# #         continue
# '#     else':'',
# #         num +=i
# #
# # print(num)
#
#
# '# def fun(str)':'',
# #     print(str)
# #     return str
# '# if __name__ == '__main__'':'',
# #     fun("熊大")
# #     fun("熊二")
# #
# #
# '# def a(x,y)':'',
# '#     if x == y':'',
# #         return x,y
# #
# # # print(a(3,3))
# # num = a(4,4)
# # print(num)
#
# # x = 1
# # y = 2
# '# def add(x,y)':'',
# #     z = x + y
# #     return z
# #
# # print(add(x,y))
# # x = 1
# # y = 2
# '# def add(x,y)':'',
# #     z = x + y
# #     print(z)
# #     return "ok"
# #
# # print(add(x,y))
#
#
# '# def lazy(*args)':'',
# '#     def num()':'',
# #         x = 0
# '#         if n in args':'',
# #             x = x+n
# #         return x
# #     return num
# #
# '# if __name__ == '__main__'':'',
# #
# #     f = lazy(1,2,3,4,5,6)
# #     # print(type(f))
# #     print(f())
# #
# # import os
# # val = os.system('ls -al')
# # print(val)
#
#
#
# # import requests
# '# response = requests.get("https':'//www.baidu.com")',
# # print(response)
#
# #
# # import requests
# # kw = {'wd','长城'}
# '# headers = {"User-Agent"':' "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}',
# #
# '# respose = requests.get("http':'//www.baidu.com/s?", params = kw, headers = headers)',
# # print(respose.text)
# # #
# # # # print(respose.content)
# # #
# # # print(respose.url)
# # # print(respose.encoding)
# #
# # print(respose.status_code)
#
#
# # import requests
# #
# # auth = {"yzq","111."}
# #
# '# repose = requests.get("https':'//bweb.wutoon.com/f061503/status")',
# #
# # # print(repose.text)
# # print(repose.status_code)
#
#
#
# # f = open("user.txt",encoding="UTF-8")
# # print(f.read())
# #
# # # f.write("爱我中华")
# # print(f.read())
#
#
# # f = open("xiao.txt","w",encoding="UTF-8")
# #
# # f.write("滨合云智")
# # f.close()
# #
# # z = open("xiao.txt",encoding="UTF-8")
# # print(z.read())
# #
# # f = open("xiao.txt","w",encoding="UTF-8")
# # f.write("天下太平")
# # f.write("平台先\n")
# # f.write("区块链\n")
# # f.write("独角兽\n")
# # f.close()
# # z = open("xiao.txt",encoding="UTF-8")     #默认为r模式
# # print(z.read())
#
# '# with open(r"xiao.txt","r",encoding="UTF-8") as f':'',
# #     print(f.readline())             #光标的概念
# #     print("=================")
# #     print(f.read())
# #
# '# with open(r"xiao.txt","a",encoding="UTF-8") as f':'',
# #     f.write("杭州区块链")
#
# #
# '# with open(r"xiao.txt","a+",encoding="UTF-8") as f':'',
# #     f.write("杭州区块链\n")
# #     f.write("存储技术有限公司\n")
# #     f.write("江干区\n")
# #     print(f.readlines())
#
#
# '# with open("xiao.txt","r+",encoding="UTF-8") as f':'              #循环文件',
# '#     for  line in f':'             #每循环一次，读一行',
# #         line = line.split()
# #         print()
# #         print(line,end="")
#         # height = line[2]
# '#         # print("每个人的身高分别是':'", height)',
# #
# # f1 = open("xiao.txt",encoding="UTF-8")
# # f2 = open("user.txt",encoding="UTF-8")
#
# # f3 = f2.readline()
# # # print(f3)
# #
# '# for line in f1.readlines()':'',
# '#     if f3 in line':'',
# #         print("包含")
# #         # print(f3)
# '#     else':'',
# #         print("不包含")
# #         # print(f3)
# #
# # f1 = open("xiao.txt",encoding="UTF-8")
# # f2 = open("user.txt",encoding="UTF-8")
# # # print(f1.read())
# # # print(f2.read())
# # print(f1.readline())
# # print(f1.readline())
#
# '# if f2.read() in f1.read()':'',
# #     print("包含")
# '# else':'',
# #     print("不包含")
#
#
#
# # f = open("xiao.txt","r+",encoding="UTF-8")
# # print(f.read())
# # print(f.tell())
# #
# #
# #
# # f = open("xiao.txt","r+",encoding="UTF-8")
# # da = f.read()
# # print(da.replace("马千雨","丑八怪"))
#
#
#
#
#
# #函数
# '# def cl(name,age)':'',
# #     print(f"my name is {name},my age is {age}")
# #
# # cl("alex",12)
#
#
#
# '# def regis(name,age,*args,**kwargs)':'      #args是个元组，可以写多个参数  **kwargs是个字典',
# #     print(name,age,args,kwargs)
# #
# # regis("alex",22,110,"杭州",tell=15867630863,zai="江干")
#
# '# def print_info(name,age,*args,**kwargs)':'',
# #     print(name,age,args,kwargs)
# #
# # print_info("jack",22,"爱你吗的麻花请",addr="hangzhou",from_addr="taizhou")
#
#
# '# def info(name,age,sourse="python",**kwargs)':'',
# # #     print("======个人信息======")
# # #     print(name)
# # #     print(age)
# # #     print(sourse)
# # #     print(kwargs)
# '# #     if age > 30':'',
# # #         return False
# '# #     else':'',
# # #         return True
# # #
# # #
# # # a = info("alex",22,addr="hanzghou",zuji="shandong")
# '# # if a':'',
# # #     print("注册成功")
# '# # else':'',
# # #     print("nono")
#
# # name = "alex is"
# '# def nn()':'',
# #     name = "jack"
# #     print(f"现在是什么名字，{name}")
# #
# # nn()
# # print(name)
#
#
# '# def saa(name,age)':'',
# #     print(f"my name is {name},age is {age}")
# #
# # saa("alex",12)
#
# #
# # import os
# #
# # os.mkdir("hello")
# #
# # from os import system
# # system("dir")
#
# #
# #
# #
# # # my_module_test.z()
# # import sys
# # import os
# # # print(sys.path)
# #
# '# def sw()':'',
# #     print("我是函数里面的")
# #
# # # print("我是函数外面的")
# #
# # print(__file__)                                    #打印当前脚本的文件路劲
# # print(os.path.dirname(os.path.dirname(__file__)))
#
#
# # import sys
# # print(sys.path)
#
# #
# # from os import system
# # system("time dir")
#
# #
# # import os
# # print(os.path.dirname(__file__))
# # import random
# # print(random.random())
#
# # from openpyxl import Workbook           #Workbook创建xlsx
# # from openpyxl import load_workbook      #加载已经存在的文件
# #
# # wb =  Workbook()  #创建exls 在内存里
# # sheet = (wb.active)
# # print(sheet.title)
# #
# # sheet.title = "姑娘们出来接客了"        #标签命名
# # sheet["B7"] = "3号技师"
# # sheet["B8"] = "20快"
# # sheet.append(["4号技师","190斤","170cm"])
# #
# # wb.save("girl.xlsx")
#
#
# #
# # # wb = load_workbook("")
# #
# #
# # from openpyxl import Workbook,load_workbook
# #
# # wb = load_workbook("ceshi.xlsx")
# #
# # # print(wb.sheetnames)
# # # print(wb.get_sheet_names())
# # sheet = wb.get_sheet_by_name("Sheet1")
# #
# # print(sheet["C7"].value)        #获取单元格的值
# '# # print(sheet["C7':'C19"])',
# #
# '# # for cell in sheet["C7':'C19"]:      #获取指定列的切片数据',
# # #     print(cell[0].value)
# #
# '# for row in sheet':'           #循环全部',
# #     # print(row)
# '#     for cell in row':'',
# #         print(cell.value,end=",")
# #     print()
#
# # import requests
# #
# '# url = "https':'//www.sogou.com/"',
# # response = requests.get(url=url)
# # # print(response.text)
# '# with open("sougou.html","w",encoding="UTF-8") as f':'',
# #     f.write(response.text)
# #     print("爬取结束")
#
#
#
#
#
# # import requests
# #
# '# url = "https':'//www.sogou.com/web"',
# # #处理url携带的参数
# #
# # #UA伪装： 让爬虫对应的请求伪装成浏览器
# '# kw = input("请输入您想搜的词':' ")',
# #
# # header = {
# '#     'User-Agent'':' "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"',
# # }
# #
# # param = {
# '#     'query'':'kw',
# # }
# # respone = requests.get(url=url,params=param,headers=header)
# # page_text = respone.text
# # fileName = kw + '.html'
# '# with open(fileName,"w",encoding="UTF-8") as f1':'',
# #     f1.write(respone.text)
# #
#
#
#
# # import requests
# #
# '# url = "https':'//filfox.info/"',
# '# kk = input("您想查什么节点':' ")',
# # param = {
# '#     'query'':' kk',
# # }
# # header = {
# '#     "User-Agent"':' "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"',
# # }
# # fan = kk + ".html"
# # response = requests.get(url=url,params=param,headers=header)
# # print(response.text)
# '# with open(fan,"w",encoding="UTF-8") as f':'',
# #     f.write(response.text)
# #
# # print(fan,"爬取结束")
#
#
# # import requests
# # import json
# # header = {
# # '#     "User-Agent"':' "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"',
# # # }
# # '# post_url= "https':'//fanyi.baidu.com/sug"',
# # '# inn = input("您要查询的词':' ")',
# # # data = {
# # '#     "kw"':' inn',
# # }
# #
# # response = requests.post(url=post_url,data=data,headers=header)
# #
# # # print(response.json())              #json方法返回的是object，如果确定访问的服务器是json类型才可以用这个方法
# # dic_obj = response.json()
# #
# # ax = inn + ".json"
# #
# # f = open(ax,"w",encoding="UTF-8")
# # json.dump(dic_obj,fp=f,ensure_ascii=False)
# # print("over......")
#
# import requests
# from requests.auth import HTTPBasicAuth
# from bs4 import BeautifulSoup
# url = "https':'//bweb.wutoon.com/f061503/status"
# auth = requests.auth.HTTPBasicAuth("yzq","111.")
# #
# response = requests.get(url=url,auth=auth)
# print(response.text)
# # zao = open("zao.html","w",encoding="UTF-8")
# # zao.write(response.text)
#
# # import requests
# #
# '# url = "http':'//scxk.nmpa.gov.cn:81/xk/"',
# #
# # header = {
# '#     "User-Agent"':' "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"',
# # }
# # page_text = requests.get(url=url,headers=header).text
# # print(page_text)
# #
# # '# with open("hua.html","w",encoding="UTF-8") as f':'',
# # #     f.write(page_text)
# #
# #
# # 'on':' true',
# # 'page':' 1',
# # 'pageSize':' 15',
# # 'productName':'',
# # 'conditionType':' 1',
# # 'applyname':'',
#
#
#


# ex = '<div class="thumb">.*?<img src="(.*?) alt.*?</div>'


from bs4 import BeautifulSoup
import os
#将本地的html文档中的数据加载到对象中
datta = open("xinwen.html","r+",encoding="UTF-8")
soup = BeautifulSoup(datta,'lxml')
# print(soup.li)                  #soup.tagName 返回html中第一次出现的标签
# print(soup.find("li"))
# print(soup.find_all("li"))

# print(soup.find_all("li"))

# print(soup.select('li'))












