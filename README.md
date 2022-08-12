# WZXY-health-report-reminder
我在校园打卡提醒脚本，自动将打卡提醒消息发送至班级QQ群，督促同学进行每日健康打卡。需要班委权限账号，如没有，请联系辅导员开通。
## 使用方法：
1. 需要一台具有公网访问权限的计算机，无需公网IP。在本机后台配置好go-cqhttp，工作在5700端口，不设加密，后台运行（使用screen或nohup）。推荐防火墙不要开放5700端口。
2. 在accountManage.py里设置好具有班委权限的账号和密码。
3. 在cardRemind.py设置发送提醒的QQ群。
4. 在服务器上设置计划任务，定期执行python3 cardRemind.py
本脚本具有暂存用户标识的功能，避免频繁登录被封号，但只支持单账号使用。如需使用多账号，请复制多份使用。

![image]('https://github.com/xiazhuozhao/WZXY-health-report-reminder/blob/802db4da25d389f212a92efbb7dd4ca261f1de22/pics/1.png')

![image]('https://github.com/xiazhuozhao/WZXY-health-report-reminder/blob/802db4da25d389f212a92efbb7dd4ca261f1de22/pics/2.png')
