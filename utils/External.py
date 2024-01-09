import datetime
import re
import os
import shutil

def process_bar(percent, start_str='', end_str='', total_length=0):
    bar = ''.join(["\033[31m%s\033[0m"%'   '] * int(percent * total_length)) + ''
    block = int(round(percent,2)*100)//(100//total_length)
    space = total_length - block
    bar = '\r' + start_str + block*'#'+ space*'-' + ' {:0>4.1f}%|'.format(percent*100) + end_str
    print(bar, end='', flush=True)

def PrettyXml(element, indent='\t', newline='\n', level=0):
    """
    xml文件规范化
    来源：https://blog.csdn.net/u012692537/article/details/101395192
    """

    if element:
        if (element.text is None) or element.text.isspace():
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
    temp = list(element)
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):
            subelement.tail = newline + indent * (level + 1)
        else:
            subelement.tail = newline + indent * level
        PrettyXml(subelement, indent, newline, level=level + 1)

def re_search(rule, text):
    try:
        block = re.search(rule, text).span()
        res = text[block[0]:block[1]]
        return (res,block[1])
    except:
        return None

def get_date():
    return datetime.date.strftime('%Y%m%d')

def remakedir(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)