import urllib

import xlrd
from io import BytesIO
from urllib.request import urlopen
import os
import requests


def read():
    data = xlrd.open_workbook("./1.xls")
    table = data.sheets()[0]
    nRow = table.nrows
    print(nRow)
    for i in range(1, nRow):
        r = table.row_values(i, start_colx=0, end_colx=None)
        dirname = 'oa'
        url = r[1]
        name = r[0]
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        response = requests.get(url)
        filename = dirname + '/' + name + '.jpg'
        # print(name)
        print(i)
        with open(filename, 'wb') as f:
            f.write(response.content)


def read2():
    data = xlrd.open_workbook("./1.xls")
    table = data.sheets()[0]
    nRow = table.nrows
    print(nRow)
    for i in range(155, nRow):
        r = table.row_values(i, start_colx=0, end_colx=None)
        dirname = 'oa'
        title = r[0]
        file_url = r[1]
        file_list = file_url.split('/')
        pre_name = file_list[len(file_list) - 1]
        last_name = pre_name.split('.')[1]
        key_url = r[2]
        center = r[3]
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        response1 = requests.get(file_url)
        response2 = requests.get(key_url)
        title = title.replace('/','\\')
        filename1 = dirname + '/' + center + '_' + title + '_无密码.' + last_name
        filename2 = dirname + '/' + center + '_' + title + '_有密码.' + last_name
        print(filename1)
        with open(filename1, 'wb') as f:
            f.write(response1.content)
        with open(filename2, 'wb') as f:
            f.write(response2.content)
        print(i)

read2()
