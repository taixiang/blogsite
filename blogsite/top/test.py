def test():
    str1 = []
    file_1 = open("7.txt", "r", encoding="utf-8")
    for line in file_1.readlines():
        str1.append(line.replace(',','\n'))

    for str in str1:             #去重后的结果写入文件

        with open("8.txt","a+",encoding="utf-8") as f:
            f.write(str + "\n")

def format():
    str1 = []
    file_1 = open("1.txt", "r", encoding="utf-8")
    for line in file_1.readlines():
        line1 = line.replace('BT', '')
        line2 = '\"' + line1
        new_line = line2.replace('\n', '\",')
        str1.append(new_line)

    for str in str1:

        with open("7.txt","a+",encoding="utf-8") as f:
            f.write(str + "\n")

def expressData():
    expressList = []
    shipperCodeList = []
    logisticCodeList = []
    file_1 = open("2.txt", "r", encoding="utf-8")
    for line in file_1.readlines():
        line1 = line.replace('\n', '')
        shipperCodeList.append(line1)

    file_2 = open("3.txt", "r", encoding="utf-8")
    for line in file_2.readlines():
        line1 = line.replace('\n', '')
        logisticCodeList.append(line1)

    for i in range(len(shipperCodeList)):
        express = {}
        express["ShipperCode"] = shipperCodeList[i]
        express['LogisticCode'] = logisticCodeList[i]
        expressList.append(express)

    print(expressList)

def qq():
    file_1 = open("4.txt", "r", encoding="utf-8")

format()