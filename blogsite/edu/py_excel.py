import xlrd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogsite.settings")
django.setup()
from edu.models import Question

data = xlrd.open_workbook("./yuwen.xlsx")
table = data.sheets()[0]
nRow = table.nrows
nCol = table.ncols

# 记录空题目
file_empty = open('empty.txt', 'a', encoding='utf-8')

for i in range(1, nRow):
    r = table.row_values(i, start_colx=0, end_colx=None)
    if len(r[0]) > 0:
        if len(r[6]) <= 0:
            file_empty.write("第" + str(i) + "行")
        ques = Question()
        ques.title = r[0]
        ques.optA = r[1]
        ques.optB = r[2]
        ques.optC = r[3]
        ques.optD = r[4]
        ques.point = r[5]
        ques.correct = r[6]
        ques.analyze = r[7]
        ques.type_id = 1
        ques.save()
        # for j in range(nCol):
        # print(i, j, str(table.row_values(i)[j]))
