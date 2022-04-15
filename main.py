import requests, time

# 在下方填写你的我在校园用户名或密码
username = ""
password = ""

#在下方填写你需要提醒的QQ群号
QQgroup = ""


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
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2006J10C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3141 MMWEBSDK/20210601 Mobile Safari/537.36 '
                      'MMWEBID/7602 MicroMessenger/8.0.7.1920(0x28000753) Process/appbrand0 WeChat/arm64 Weixin '
                      'NetType/WIFI Language/zh_CN ABI/arm64 miniProgram',
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
        url = "https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username?username=%s&password=%s"%(username, password)
        headers = {
            'Host': 'gw.wozaixiaoyuan.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI '
                          'MiniProgramEnv/Windows WindowsWechat',
            'Content-Type': 'application/json;charset=UTF-8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://gw.wozaixiaoyuan.com/h5/mobile/basicinfo/index/login/index?jwcode=1002&openId=o0'
                       '-5d1u2EhvJvv7rSsp68lvKbnc4&unionId=oUXUs1S5gFViHuIPrPj7Zo6w8DgU',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us,en',
        }
        session = requests.session()
        a = session.post(url, headers=headers, data={})
        print(a.text)
        try:
            print(requests.utils.dict_from_cookiejar(session.cookies)['JWSESSION'])
            with open("JWSESSION", "w") as f:
                f.write(requests.utils.dict_from_cookiejar(session.cookies)['JWSESSION'])
        except:
            return False


def cardReport():
    return 1


def getUnreportedList():
    datestr = time.strftime("%Y%m%d", time.localtime(time.time()))
    url = "https://student.wozaixiaoyuan.com/health/getHealthUsers.json"
    with open("JWSESSION") as f:
        JWSESSION = f.read()
    headers = {
        'Host': 'student.wozaixiaoyuan.com',
        'Connection': 'keep-alive',
        'Cookie': '',
        'JWSESSION': JWSESSION,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI '
                      'MiniProgramEnv/Windows WindowsWechat',
        'content-type': 'application/x-www-form-urlencoded',
        'token': '',
        'Referer': 'https://servicewechat.com/wxce6d08f781975d91/181/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    data = "type=0&date=" + datestr
    state = dict(requests.post(url, headers=headers, data=data).json())['data']
    print(state)
    output = "自动提醒：截止目前，"
    if state:
        for p in state:
            output += p['name'] + '(%s, %s)， '%(p['number'], p['phone'])
        output += "还没有进行每日健康填报，请尽快完成，以免带来不便。如有错误请告知。"
        requests.get("http://127.0.0.1:5700/send_group_msg?group_id=%s&message="%QQgroup + output)
    else:
        output += "所有同学已完成每日健康填报。"
    print(output)


if __name__ == "__main__":
    login()
    getUnreportedList()
