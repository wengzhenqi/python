import requests
import json
post_url = "https://fanyi.baidu.com/sug"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
pa = input("输入你想翻译的内容： ")
data = {
    'kw': pa
}
response = requests.post(url=post_url,data=data,headers=header)
print(response.json())
dic_ocj = response.json()
fp = open("./dog.json","w",encoding="UTF-8")
json.dump(dic_ocj,fp=fp,ensure_ascii=False)
print("over...")