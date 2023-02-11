# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 4:24 PM
# @Author  : chenting
# @File    : get_cookie.py
# @Software : PyCharm
import json
import time
from datetime import datetime

from jira import JIRA



class GetBugs:
    #定义类属性
    jira = JIRA(server="https://jira.newbanker.cn/", auth=("chenting", "newbanker@123"))

    # def get_project(self):#获取项目
    #     # myself = jira.myself()
    #     project1=self.jira.projects()#查询出所所有的项目
    #     print(project1)
    #     for key in project1:
    #         project=self.jira.project(key)
    #         if project.name=="建信基金":
    #             return project.name

    def get_bugs(self):#获取所有bug,筛选状态为Done的数据并发送邮件到企业邮箱
        # issue = self.jira.issue('建信基金')
        jql = 'project="建信基金"'
        issues = self.jira.search_issues(jql)#查找制定项目的问题数据
        list=[]
        for key in issues:
            # print(key)
            issue = self.jira.issue(key)
            summary = issue.fields.summary #获取标题
            status = issue.fields.status #获取缺陷状态
            # print(type(status))
            created_data=issue.fields.created #缺陷创建时间
            update_date=issue.fields.updated#缺陷更新时间
            createdor=issue.fields.creator #创建人
            handle_or=issue.fields.assignee#经办人
            time_now=time.strftime("%Y-%m-%d %H:%M:%S")
            # print(key,summary,status,createdor,created_data,handle_or,update_date)

            if str(status) == 'IN REVIEW':
                # print(summary,status)
                # print(key, summary, status, createdor, created_data, handle_or, update_date)
                list.append({"key":str(key), "summary":str(summary), "status":str(status), "createdor":str(createdor), "created_data":str(created_data), "handle_or":str(handle_or), "update_date":str(update_date)})

        return list



if __name__ == '__main__':
    a=GetBugs()
    # print(a.get_project())
    h=a.get_bugs()
    print(h)

    # print(type(a))





