import requests
import re
import json
import py2ifttt
from py2ifttt import IFTTT
import datetime

def get_code_name(code):
    headers = {'referer': 'http://finance.sina.com.cn'}
    if code[:2] == '60':
        code = 'sh' + code
    elif code[:2] == '30':
        code = 'sz' + code
    elif code[:2] == '00':
        code = 'sz' + code
    elif code[:2] == '68':
        code = 'sh' + code
    url = f"http://hq.sinajs.cn/list={code}"
    response = requests.get(url, headers=headers)
    text = response.text
    codename = re.search(r'[\u4e00-\u9fa5]+', text).group()
    return codename

def create_text_cnsp(code_score_list, date, msg=""):
    text = f"<br/>{datetime.datetime.now()}<br/>{date}<br/><br/>" + "="*20 + "<br/>"
    text += "code\t\tname\t\tsocre\t\tpvp<br/>"
    for ix, (code, score, pvp) in enumerate(code_score_list):
        print(code, score, pvp)
        text += f"{code}\t\t{get_code_name(code)}\t\t{round(float(score), 2)}\t\t{pvp}<br/>"
    text += "="*20 + "<br/>"
    text += msg
    return text


def create_text_cnp(code_list):
    text = f"<br/>{datetime.datetime.now()}<br/><br/>" + "="*20 + "<br/>"
    text += "code\t\tname\t\tpvp<br/>"
    for ix, (code, pvp) in enumerate(code_list):
        print(code, pvp)
        text += f"{code}\t\t{get_code_name(code)}\t\t{pvp}<br/>"
    text += "="*20 + "<br/>"
    return text

def create_text_c(code_list):
    text = f"<br/>{datetime.datetime.now()}<br/><br/>" + "="*20 + "<br/>"
    for ix, code in enumerate(code_list):
        print(code)
        text = text + f"{code}\t" + ("<br/>" if ix % 2 == 0 else "\t")
    text += "="*20 + "<br/>"
    return text

class Ifttt():
    
    def __init__(self, key="c5fQLgMhc1JhwzJyH7dNVDcRocfBDn3S080z3a5fQBl", event_name="gpsm"):
        self.ifttt = IFTTT(key=key, event_name=event_name)
        
    def send_cnsp(self, code_score_list, date="None", msg=""):
        text = create_text_cnsp(code_score_list, date, msg)
        self.ifttt.notify(value1=text)
        print(f"[{datetime.datetime.now()}] IFTTT message was sent.")

    def send_cnp(self, code_list):
        text = create_text_cnp(code_list)
        self.ifttt.notify(value1=text)
        print(f"[{datetime.datetime.now()}] IFTTT message was sent.")

    def send_c(self, code_list):
        text = create_text_c(code_list)
        self.ifttt.notify(value1=text)
        print(f"[{datetime.datetime.now()}] IFTTT message was sent.")