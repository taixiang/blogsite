import xlrd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogsite.settings")
django.setup()
from edu.models import Ques, Mission

data = xlrd.open_workbook("./test.xlsx")
table = data.sheets()[0]
nRow = table.nrows
nCol = table.ncols
for i in range(1, nRow):
    r = table.row_values(i, start_colx=0, end_colx=None)
    print(r)
    mis = Mission.objects.get_or_create(level=int(r[7]), type_id=1)[0]
    print(mis)
    ques = Ques()
    ques.title = r[0]
    ques.optA = r[1]
    ques.optB = r[2]
    ques.optC = r[3]
    ques.optD = r[4]
    ques.correct = r[5]
    ques.type_id = int(r[6])
    ques.level_id = mis
    ques.save()
    # for j in range(nCol):
    # print(i, j, str(table.row_values(i)[j]))
