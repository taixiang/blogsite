import urllib

import xlrd
from io import BytesIO
from urllib.request import urlopen
import os
import requests


def read():
    data = xlrd.open_workbook("./all.xls")
    table = data.sheets()[0]
    nRow = table.nrows
    print(nRow)
    for i in range(1, nRow):
        r = table.row_values(i, start_colx=0, end_colx=None)
        dirname = r[0]
        url = r[3]
        name = r[2].replace("/", "-")
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        response = requests.get(url)
        filename = dirname + '/' + name + '.jpg'
        print(name)
        print(i)
        with open(filename, 'wb') as f:
            f.write(response.content)


read()
