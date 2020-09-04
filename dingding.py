#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/4 9:11
# @Author : zheng
# @Site : 
# @File : dingding.py
import json
import requests

def message(link=1):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=84e7e98c7e1322c1ec9b614c1c99a72f5579a9c0be5cd1742cca8d8a50735454'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "：%s " % ('请告诉我一个小秘密，你的测试报告搞完没？')
        },
        "at":{
            "atMobiles":[
                "17637870610"       #需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": True     #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    message()