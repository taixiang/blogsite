import xlrd


def agData():
    names_ag = ['许亮', '朱涵威', '高永柳', '彭玲', '王都胜',
                '赵玮', '王锐健', '袁艺', '张凯', '薛飞',
                '曲虎鹏', '徐星', '赵俊', '冯美子', '黄春贞',
                '马云凤', '李武龙', '马光旭', '朴永鹤', '王惠娟',
                '王启超', '谢佳', '马丙强', '林雨彬', '杨洁',
                '张泽鹏', '樊杰', '赵志军', '赵吉', '段永菊',
                '葛杨', '田晨', '王南', '王瑶', '赵启霞',
                '黄新雨', '林炳炎', '王海靖', '方建兵', '赵兵',
                '张云',
                '赵晨浩', '任芮', '豆永坤', '吴孝辰', '张健',
                '张宁', '张艳梅', '朱秀国', '陈海涛', '林雨鸿',
                '曲晓伟', '庄强', '吴燕', '施涛', '王锡利',
                '高盖', '王成', '吕迎春', '芮金根', '葛磊',
                '王赛', '朱云霞', '胡楠', '万小林', '张宝云',
                '张敏', '朱玲', '徐家文', '刘卫华', '赵毅',
                '王丽娜', '周虹', '张都帅', '朱宗旺', '张光军',
                '朱丽萍', '吴亚军', '黄瓒', '吴雪利', '张贞芳',
                '赵敬阳', '戎孟雨', '邵明远', '徐泓达', '王先文',
                '王启龙', '邰祥', '徐西珍', '江翠', '周谦',
                '戴丽', '吴小宝', '韦家志', '朱素兰', '王俊菲',
                '杜金河', '王亚飞', '杨孟雅', '胡金芝', '刘凯',
                '蔡梦', '刘胜杰', '王楠', '张鑫', '朱倩媛',
                '袁野', '赵伟方', '娄玉', '刘鹏', '赵宁宁',
                '董兴辉', '张越', '朱庆义', '樊晓兵', '绳凤',
                '王刚',
                '樊秋茹', '彭正聪', '王键', '张峰华', '肖双娥',
                '孙波', '陈勇', '董国荣', '段元通']
    moneys_ag = []
    data_ag = []
    excel = xlrd.open_workbook("test.xls")
    excel.sheet_names()  # 获取excel里的工作表sheet名称数组
    sheet = excel.sheet_by_index(0)  # 根据下标获取对应的sheet表
    names = sheet.col_values(2)  # 获取第一列的数据
    money = sheet.col_values(9)
    for i in range(0, sheet.nrows):
        # 表格里的数据
        name = sheet.cell(i, 2).value
        if name in names_ag:
            data = (name, (float)(sheet.cell(i, 9).value))
            data_ag.append(data)
            # print(i + 1)
            # print(name)

    new_data_ag = sorted(data_ag, key=lambda s: s[1], reverse=True)
    # print(new_data_ag)

    print(new_data_ag[-20:])
    #
    # for i in range(len(new_data_ag), -1, -1):
    #     print(i)
    #     continue



agData()
