import requests
import time
from accountManage import login, getUA

# 打卡提醒群号
group_1 = ""
# 全部同学已经打卡完成，发送提示信息的群号
group_1 = ""

def getUnreportedList():
    #datestr = "20211106"
    datestr = time.strftime("%Y%m%d", time.localtime(time.time()))
    path = "/health/mobile/manage/getUsers?date=" + \
        datestr+"&batch=5600001&page=%d&size=20&state=1&keyword=&type=0"
    with open("JWSESSION") as f:
        JWSESSION = f.read()

    output = ""
    unreportedPeople = []

    for i in range(1,4):
        url = "https://gw.wozaixiaoyuan.com"+ path % i
        headers = {
            'Host': 'gw.wozaixiaoyuan.com',
            'Connection': 'keep-alive',
            'Cookie': 'JWSESSION=%s'%JWSESSION,
            'User-Agent': getUA(),
            'content-type': 'application/x-www-form-urlencoded',
            'token': '',
            'Referer': "https://gw.wozaixiaoyuan.com/h5"+ path % i,
            'Accept-Encoding': 'gzip, deflate, br'
        }
        state = dict(requests.get(url, headers=headers).json())['data']
        try:
            for each in state:
                unreportedPeople.append(each['name'])
        except:
            pass
        # print(state)
        # print(unreportedPeople)

    if unreportedPeople:
        for p in unreportedPeople:
            output += p + '， '
        output += "请进行健康打卡。"
        requests.get("http://127.0.0.1:5700/send_group_msg?group_id=%s&message=" % group_1 + output)
    else:
        output += "所有同学已完成每日健康填报。"
        requests.get("http://127.0.0.1:5700/send_group_msg?group_id=%s&message=" % group_2 + output)
    print(output)


if __name__ == "__main__":
    login()
    getUnreportedList()
