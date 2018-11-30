import xlrd
import time


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[9]


def word():
    goods_list = []
    workbook = xlrd.open_workbook("2.xls")
    sheet = workbook.sheet_by_index(0)
    v_1 = sheet.row_values(0)
    print(v_1)
    cur_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(cur_time)

    for i in range(1, sheet.nrows):
        v = sheet.row_values(i)
        # if v[19] >= cur_time:
        #     print(v[19])
        goods_list.append(v)

    goods_list.sort(key=lambda x: float(x[9]), reverse=True)
    for i in goods_list:
        print((i[9]))


word()
