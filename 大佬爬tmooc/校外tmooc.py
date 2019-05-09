#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# author:lvusyy   (https://github.com/lvusyy)
import copy
import os
import re
import time
import sys
import bs4
import requests

# by:lvusyy
# 请先阅读readme.md
# node :  安装依赖包. 还需安装 ffmpeg http://ffmpeg.org/

# ----------
# 自定义配置区域
startCourse = 106  #  修改此字段可以设置从第几个视频开始下载
path = os.path.dirname(os.path.abspath(__file__))
#path = “/root/video/” or "d:\video\"        #"指定保存文件的目录  绝对路径哦"
# ----------


headers = {
    'Origin': 'http://tts.tmooc.cn',
    'Referer': 'http://tts.tmooc.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
    'Cookie': 'eBoxOpenNSDTN201801=true; .local.language=zh-CN; UM_distinctid=167834f96cd21a-0be45a32cfd683-3976045e-1fa400-167834f96ce10bf; Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1557105553,1557147096,1557147604,1557363488; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1557363488; TMOOC-SESSION=1B24A33A1A6A4A2C9F8CC514CD1ECBFE; sessionid=1B24A33A1A6A4A2C9F8CC514CD1ECBFE|E_bfulu70; cloudAuthorityCookie=0; versionListCookie=NSDTN201801; defaultVersionCookie=NSDTN201801; versionAndNamesListCookie=NSDTN201801N22NLinux%25E4%25BA%2591%25E8%25AE%25A1%25E7%25AE%2597%25E5%2585%25A8%25E6%2597%25A5%25E5%2588%25B6%25E8%25AF%25BE%25E7%25A8%258BV06; courseCookie=LINUX; stuClaIdCookie=659284; JSESSIONID=8ABCBAA8E8CB16EAF8FB87B21D050ACC; tedu.local.language=zh-CN; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1557363506,1557363530,1557373613,1557378168; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1557378168; isCenterCookie=yes'
}
rsp = requests.session()

rsp.headers = copy.deepcopy(headers)
tm = ''
CenterVideoUrl = 'http://videotts.it211.com.cn/'
outSideVideoUrl = 'http://c.it211.com.cn/'
videoUrl = CenterVideoUrl
# out or center
try:
    if rsp.get('http://videotts.it211.com.cn/isCenter.html', timeout=1500).status_code != 200:
        videoUrl = outSideVideoUrl
        print('校外模式！')
except:
    videoUrl = outSideVideoUrl
    print('校外模式！')


# path="/home/makeit/youPATH"


def merge(file):
    '合并mp4文件'
    # file is m3u8 type
    # amorpm = file.replace('.m3u8', '')[-2::]
    amorpm = file.replace('.m3u8', '').split(os.path.sep)[-1]
    if os.path.exists(file):
        filecontent = ''
        f = open(file, "r")
        if f.read().find("http") != -1:
            f.seek(0, 0)
            # f = open(file, "r")
            for i in f.readlines():
                if i.find("http") != -1:
                    if i.find(".key") != -1:
                        filecontent += '#EXT-X-KEY:METHOD=AES-128,URI="'
                    # filecontent += amorpm+i.split('/')[-1].replace("-", '')
                    filecontent += i.split("/")[-1].replace("-", '')

                else:
                    filecontent += i
            f.close()
            with open(file, "w") as f:
                f.write(filecontent)
            print(file + "处理完成")
        f.close()
    else:
        print('必要de m3u8文件不存在！')
        return

    dir_ = os.path.dirname(file)
    filename = file.split(os.path.sep)[-1]

    if os.path.exists(os.path.join(dir_, file.split(os.path.sep)[-2]) + "_" + amorpm + ".mp4"):
        # mp4文件已经合成过了.
        return
    
    if sys.platform=="win32":
        
        os.system("echo cd "+dir_+">> "+os.path.join(dir_,"win32Merge.bat"))
        cmd ='ffmpeg -allowed_extensions ALL -protocol_whitelist "file,http,crypto,tcp" -i ' + filename + ' -c copy video.mp4'
        with open(os.path.join(dir_,"win32Merge.bat"),"ab+") as f:
            f.write(cmd.encode())
        os.system("cmd /c "+os.path.join(dir_,"win32Merge.bat"))
        os.remove(os.path.join(dir_,"win32Merge.bat"))
    else:
        cmd = "cd " + dir_ + '; ffmpeg -allowed_extensions ALL -protocol_whitelist "file,http,crypto,tcp" -i ' + filename + ' -c copy video.mp4'
        os.system(cmd)
    
    print(file + " 处理完成!")
    try:
        os.rename(os.path.join(dir_, "video.mp4"), os.path.join(dir_, file.split(os.path.sep)[-2]) + "_" + amorpm + ".mp4")
        # 合并成功后,删除源分片的文件.防止和下次文件冲突,,,,,,,ps 实际并不会冲突,因为文件名不是一样的

        if sys.platform=="win32":
            os.system("del /f "+os.path.join(dir_,"*.ts"))
        else:
            os.system("rm -f " + os.path.join(dir_,"*.ts"))

        ##### 注意这里．合成完毕后需要删除key或重新命名文件. 但是static.key冲突. 而且改名会出错.原因未知?
        os.remove(os.path.join(dir_, "static.key"))
    except Exception:
        print("执行合并视屏文件出错!!! 为了保证数据一致性，删除已经下载的视频分片数据")
        if sys.platform=="win32":
            os.system("del /f "+os.path.join(dir_,"*.ts"))
        else:
            os.system("rm -f " + os.path.join(dir_,"*.ts"))


def downloadALLTs(ref, heads, path, tscontent, outUrl=''):
    ''
    # 解析下载文件链接

    filecontent = ''
    if hasattr(tscontent, 'text'):
        filecontent = tscontent.text
    if isinstance(tscontent, bytes):
        filecontent = tscontent.decode()
    # 1. 是有效的文件 外网类型
    # 2. 是有效的文件 内网类型
    #
    if filecontent.find("static.key") == -1 and filecontent.find("METHOD=AES-128") == -1:
        print("被解析文件无法识别.")
        return
    reresp = re.findall(r'(http.*)', filecontent)
    if reresp:
        heads['Referer'] = ref
        # heads['Cookie']=''
        for i in reresp:
            if len(i) > 8:
                filename = str(i.replace('"', "")).split("/")[-1].replace('-', '').replace('\r','')
                # amorpm=i.split('/')[-2][-2:]
                # if filename.find('static.key')!=-1 and filename.find('am') ==-1 and filename.find('pm')==-1:
                #     filename=amorpm+filename
                # 防止key 文件冲突,所以每次需要下载分片数据的时候默认就更新key文件
                if os.path.exists(os.path.join(path, filename)) and filename.find('static.key') == 0:
                    continue
                ret = rsp.get(i.replace('"', ""), headers=heads)
                content = ret.content
                # request = urllib.request.Request(i.replace('"', ""), headers=heads)
                # response = urllib.request.urlopen(request)
                # content = response.read()
                with open(os.path.join(path, filename), "wb") as f:
                    f.write(content)
                time.sleep(0.05)

    elif outUrl:  ### 废弃的代码,无用的.....
        heads = copy.deepcopy(headers)
        heads['Referer'] = ref
        heads['Origin'] = 'http://tts.tmooc.cn'
        reresp = re.findall(r'(.*ts)', filecontent)
        for i in reresp:
            ret = rsp.get(outUrl + i, headers=heads)
            content = ret.content
            filename = i
            with open(os.path.join(path, filename), "wb") as f:
                f.write(content)

    print("单个视频的所需分片资源下载完成!")


def getvideos(ref, path, url):
    '获取视屏页的视屏信息'
    videoUrls = []
    rsp.headers['Referer'] = 'http://tts.tmooc.cn/studentCenter/toMyttsPage'
    # del rsp.headers['Cookie']
    mRSP = rsp.get(url)
    bs = bs4.BeautifulSoup(mRSP.text, "html.parser")
    bs = bs.find_all('div', class_='video-list')

    for i in bs:
        p = i.find_all('p')
        for s_p in p:
            mid = s_p.get('id', False)
            if not mid:
                print(url + " 视频信息获取失败！")
                return

            mid = mid.replace('active_', '')
            mid = mid.replace('.m3u8', '')
            # if video exits   jump this

            videoFile = os.path.join(path, path.split(os.path.sep)[-1] + "_" + mid + ".mp4")
            if os.path.exists(videoFile):
                continue
            videoplaylisturl = videoUrl + mid + '/' + mid + '.m3u8'
            videoUrls.append([videoplaylisturl])

            downloadts(url, path, videoplaylisturl)

    if len(videoUrls) < 1:
        print("该页面可能没有视屏,或者登录已经失效!")


def downloadts(ref, path, url):
    '下载m3u8文件'

    # 文件已经存在就不要在保存了
    filename = url.split("/")[-1]
    if not os.path.exists(os.path.join(path, filename)):
        myheaders = copy.deepcopy(headers)
        myheaders['Origin'] = 'http://tts.tmooc.cn'
        myheaders['Referer'] = ref
        rspcontent = rsp.get(url, headers=myheaders)

        if rspcontent.status_code != 200:
            print("准备m3u8页面出错")
            return
        with open(os.path.join(path, filename), "wb") as f:
            f.write(rspcontent.content)
    else:
        # 如果不是从网络获取的就从本地获取
        with open(os.path.join(path, filename), "rb") as f:
            rspcontent = f.read()

    outurl = url.split('/')[-1]
    outurl = url.replace(outurl, "")
    downloadALLTs(ref, headers, path, rspcontent, outUrl=outurl)

    merge(os.path.join(path, filename))


def getPPT(ref, path, url):
    '下载ppt'
    hd = copy.deepcopy(headers)
    hd.pop('Referer')
    # 如果ppt.html文件存在就不下载了.跳过
    if os.path.exists(os.path.join(path, 'ppt.html')) or not url:
        return
    rst = rsp.get(url, headers=hd)
    if rst.status_code != 200:
        print(url, "ppt.html页面下载失败!")
        return
    with open(os.path.join(path, "ppt.html"), "wb") as f:
        f.write(rst.content)

    bsrst = bs4.BeautifulSoup(rst.text)
    imgs = bsrst.find_all("img")
    baseurl = url.replace('ppt.html', '')
    for i in imgs:
        try:
            imgrst = rsp.get(baseurl + i['src'], headers=hd)
            if imgrst.status_code != 200:
                raise IOError
            imgpath = i['src'].replace(i['src'].split('/')[-1], '')
            if not os.path.exists(os.path.join(path, imgpath)):
                os.mkdir(os.path.join(path, imgpath))
            with open(os.path.join(path, i['src']), 'wb') as    f:
                f.write(imgrst.content)

        except Exception:
            print("下载ppt.html图片时候出错")

    print(baseurl, "PPT页面下载完成!")


def getExercise(ref, path, url):
    '下载作业页面'
    hd = copy.deepcopy(headers)
    hd.pop('Referer')
    # 如果index_answer.html文件存在就不下载了.跳过
    if os.path.exists(os.path.join(path, 'index_answer.html')) or not url:
        return
    url = str(url).replace('.html', '') + "_answer.html"
    rst = rsp.get(url, headers=hd)
    if rst.status_code != 200:
        print(url, "作业页面下载失败!")
        return
    with open(os.path.join(path, "index_answer.html"), "wb") as f:
        f.write(rst.content)
    print("作业页面下载完成!")


def getCase(ref, path, url):
    '下载案例页面的数据和图片'
    hd = copy.deepcopy(headers)
    hd.pop('Referer')
    # 如果index.html文件存在就不下载了.跳过
    if os.path.exists(os.path.join(path, 'index.html')) or not url:
        return
    rst = rsp.get(url, headers=hd)
    if rst.status_code != 200:
        print(url, "案例页面下载失败!")
        return
    with open(os.path.join(path, "index.html"), "wb") as f:
        f.write(rst.content)

    bsrst = bs4.BeautifulSoup(rst.text)
    imgs = bsrst.find_all("img")
    baseurl = url.replace('index.html', '')
    for i in imgs:
        try:
            imgrst = rsp.get(baseurl + i['src'], headers=hd)
            if imgrst.status_code != 200:
                raise IOError
            imgpath = i['src'].replace(i['src'].split('/')[-1], '')
            if not os.path.exists(os.path.join(path, imgpath)):
                os.mkdir(os.path.join(path, imgpath))
            with open(os.path.join(path, i['src']), 'wb') as    f:
                f.write(imgrst.content)
            # jquery css
            urls = ['index.files/jquery.min.js', 'index.files/jquery.snippet.js',
                    'index.files/main.js', 'index.files/index.css', 'index.files/jquery.snippet.css']

            for urljscss in urls:
                content = rsp.get(os.path.join(baseurl, urljscss), headers=hd)
                if imgrst.status_code != 200:
                    raise IOError

                with open(os.path.join(path, urljscss), 'wb') as    f:
                    f.write(content.content)

        except Exception:
            print("下载图片时候出错")

    print("案例页面下载完成!")


def downloadOnePage(allurldata):
    '解析需要的视屏页和文档页信息'
    # [{title:"xxx",allurldata:http://xxx},{xxxx}]
    videoCount = 0
    for i in allurldata:
        videoCount += 1

        ###过滤路径中那些非法的字符
        mpath = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）)]+", "_", i.get("title", ""))

        mpath = os.path.join(path, str(videoCount) + "_" + mpath)
        # mpath = os.path.join(path, str(videoCount) + i.get("title", ""))

        if not os.path.exists(mpath):
            os.mkdir(mpath)

        if videoCount >= startCourse:
            if i.get('casePageurl', ''): getCase('', mpath, i.get('casePageurl'))
            if i.get('PPT', ''): getPPT('', mpath, i.get('PPT'))
            if i.get('videoPageurl', ''): getvideos('', mpath, i.get('videoPageurl'))  # jump this
            if i.get('ZY', ''): getExercise('', mpath, i.get('ZY'))


def main():
    # hook cookies

    rsp.headers['Cookie']=rsp.headers["Cookie"].replace("isCenterCookie=no","")+";isCenterCookie=yes; "

    # c = requests.cookies.RequestsCookieJar()
    # c.set("isCenterCookie", "yes",domain="tts.tmooc.cn")
    # rsp.cookies.update(c)
    rsp.headers['Referer'] = 'http://www.tmooc.cn/'
    if rsp.headers.get("X-Requested-With", False): del (rsp.headers["X-Requested-With"])
    mrsp = rsp.get("http://tts.tmooc.cn/studentCenter/toMyttsPage", )
    if mrsp.status_code != 200:
        print("失败!", mrsp.status_code)
        exit(1)

    bs = bs4.BeautifulSoup(mrsp.text.encode("utf-8"), 'html.parser')
    data = []
    # 获取有效区域
    # bs1=bs.find_all("div",class_="container")    # bs1[0].select("")
    # bs.find_next()
    bs = bs.find_all('li', class_="opened")

    if len(bs) < 1:
        print("没打开网页,或者登录已经失效了!")

        return

    for i in bs:
        tempdata = {}
        tempdata['title'] = i.find("p").string.replace('\t', '').replace('\r\n', '').replace(' ', '').replace('-',
                                                                                                              '_').replace(
            ',', '_')
        tempdata['title'] = tempdata['title'].replace('：', '').replace('、', '_').replace('/', '')

        for url in i.select('li > a'):
            if not hasattr(url, 'text') or not isinstance(url.text, str):
                print("解析ttspage出错!")
                return
            if url.text == "视频":
                tempdata['videoPageurl'] = url['href']
            elif url.text == "案例":
                tempdata['casePageurl'] = url['href']
            elif url.text.upper().find("PPT") != -1:
                tempdata['PPT'] = url['href']
            elif url.text == "作业":
                tempdata['ZY'] = url['href']

        data.append(tempdata)

    if len(data) > 10:
        print("解析视频下载页面完成,共{count}个记录".format(count=len(data)))

        downloadOnePage(data)


if __name__ == "__main__":
    main()
