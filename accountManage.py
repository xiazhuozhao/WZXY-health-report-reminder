import requests
import datetime
import time

userName = ""
passWord = ""

def getUA():
    return 'Mozilla/5.0 (Linux; Android 11; M2006J10C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3141 MMWEBSDK/20210601 Mobile Safari/537.36 MMWEBID/7602 MicroMessenger/8.0.7.1920(0x28000753) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram'

def login():
    url = "https://gw.wozaixiaoyuan.com/basicinfo/mobile/home/index?miniAppId=wxce6d08f781975d91&env=3"
    with open("JWSESSION") as f:
        JWSESSION = f.read()
    print(JWSESSION)
    headers = {
        'Host': 'gw.wozaixiaoyuan.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'JWSESSION': JWSESSION,
        'User-Agent': getUA(),
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://gw.wozaixiaoyuan.com',
        'X-Requested-With': 'com.tencent.mm',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://gw.wozaixiaoyuan.com/h5/mobile/basicinfo/index/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'JWSESSION=' + JWSESSION
    }
    response = requests.post(url, data={}, headers=headers)
    if "未登录" not in response.text:
        return True
    else:
        url = "https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username?username=%s&password=%s&openId=&unionId=&wxworkOpenId=&wxworkUserId=&wxworkCorpId=&phoneInfo=0____windows+nt+10.0%3B+win64%3B+x64" %(userName, passWord)
        headers = {
            'Host': 'gw.wozaixiaoyuan.com',
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=UTF-8',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': getUA(),
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://gw.wozaixiaoyuan.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://gw.wozaixiaoyuan.com/h5/mobile/basicinfo/index/login/index?jwcode=10',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        session = requests.session()
        a = session.post(url, headers=headers, data='{}'.encode('utf-8'))
        print(a.text)
        try:
            print(requests.utils.dict_from_cookiejar(session.cookies)['JWSESSION'])
            with open("JWSESSION", "w") as f:
                f.write(requests.utils.dict_from_cookiejar(session.cookies)['JWSESSION'])
        except:
            return False
        return True