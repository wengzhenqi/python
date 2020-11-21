import requests

url = "https://www.sogou.com/web"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
kw = input("请输入你想百度的内容： ").strip()
parm = {
    'query': kw
}
response = requests.get(url=url,params=parm,headers=header).text
# print(response)
filename = kw + ".html"
with open(filename,"w",encoding="UTF-8") as f:
    f.write(response)
print("over....")