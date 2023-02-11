# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 9:07 PM
# @Author  : xxxx
# @File    : send_data_wx.py
# @Software : PyCharm

import requests, base64, hashlib
from get_bugs.gain_bugs import GetBugs


class WXWorkSMS:
    def __init__(self):
        self.headers = {"Content-Type": "text/html"}
        self.send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=XXXXXXX"  # 测试机器人webhook地址
        self.auth = ('Content-Type', 'application/json')

    def send_requests(self, send_data):
        res = requests.post(url=self.send_url, headers=self.headers, json=send_data, auth=self.auth)
        print(res.json())

    def send_msg(self):
        # 发送消息
        get_bug_sms_list=GetBugs().get_bugs()
        project =GetBugs().get_project()
        # print(project)
        print(get_bug_sms_list)
        # content=

        for i in range(len(get_bug_sms_list)):
            summery=get_bug_sms_list[i]["summary"]
            createdor=get_bug_sms_list[i]["createdor"]
            mentioned_list_data="@"+createdor
            send_data = {
                "msgtype": "text",  # 消息类型，此时固定为news
                "text": {
                    "content": "@"+createdor+",你存在缺陷未验收"+summery,
                    "mentioned_list": ['@all']
                }
            }
            self.send_requests(send_data)


if __name__ == '__main__':
    sms=WXWorkSMS()
    sms.send_msg()
