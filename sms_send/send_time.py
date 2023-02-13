# -*- coding: utf-8 -*-
# @Time    : 2023/1/11 6:03 PM
# @Author  : XXx
# @File    : send_time.py
# @Software : PyCharm

"""
每日定时发送
"""
import time
import datetime
from sms_send import send_data_wx


class SendTime:

    def get_current_time(self):
        """#获取当前时间"""
        now_time = datetime.datetime.now().strftime("%H:%M:%S")  # 获取当前时间的时分秒
        # print(now_time)
        return now_time

    def send_msg_time(self):
        """每天早上11点发送缺陷提醒，以及每天下午5点发送缺陷提醒"""
        while True:
            if self.get_current_time() == "11:00:00":
                sms = send_data_wx.WXWorkSMS()
                sms.send_msg()
                break
            elif self.get_current_time() == "17:30:00":
                sms = send_data_wx.WXWorkSMS()
                sms.send_msg()
                break




# if __name__ == '__main__':
#     get_current_time()
