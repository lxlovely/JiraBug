# -*- coding: utf-8 -*-
# @Time    : 2023/1/12 10:33 AM
# @Author  : chenting
# @File    : run.py
# @Software : PyCharm

from sms_send.send_time import SendTime

if __name__ == '__main__':
    send_time=SendTime()
    send_time.send_msg_time()

