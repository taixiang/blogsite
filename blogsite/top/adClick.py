import os
import time
import random


def click():
    count = 0
    while True:
        if count == 20:
            return
        # 淘宝 537 1436 第二个
        # 淘宝 537 1463 第三个
        os.system('adb shell input tap 537 1463')
        print('详情')
        time.sleep(30)
        # 返回
        os.system('adb shell input keyevent 4')
        print('返回')
        count += 1
        time.sleep(10)
        print(str(count) + "完成")


# 第二个页面 浏览商品 淘宝618
# os.system('adb shell input tap 670 654')

# 第一个任务
# os.system('adb shell input tap 901 954')
# 第二个任务
# os.system('adb shell input tap 537 1165')

# 第三个任务
# os.system('adb shell input tap 396 1365')


# 京东
# os.system('adb shell input tap 884 1213')


def clickJD():
    count = 0
    while True:
        if count == 5:
            return
        # 京东 866 1175 852 164 863 1622
        # 第二个 866 1175
        # 第4个 866 1635
        # 第5个 866 1849
        os.system('adb shell input tap 866 1849')
        #浏览
        # os.system('adb shell input tap 670 654')

        print('详情')
        time.sleep(30)
        # 返回
        os.system('adb shell input keyevent 4')
        print('返回')
        time.sleep(10)
        # 领取
        # os.system('adb shell input tap 875 1695')
        # print('领取')
        # time.sleep(10)
        count += 1
        print(str(count) + "完成")

def clickJD2():
    os.system('adb shell input tap 255 840')
    print('详情1')
    time.sleep(5)
    os.system('adb shell input keyevent 4')
    print('返回')

    time.sleep(5)

    os.system('adb shell input tap 778 805')
    print('详情2')
    time.sleep(5)
    os.system('adb shell input keyevent 4')
    print('返回')

    time.sleep(5)

    os.system('adb shell input tap 255 1517')
    print('详情3')
    time.sleep(5)
    os.system('adb shell input keyevent 4')
    print('返回')
    time.sleep(5)


    os.system('adb shell input tap 778 1530')
    print('详情4')
    time.sleep(5)
    os.system('adb shell input keyevent 4')
    print('返回')

    time.sleep(5)


    os.system('adb shell input tap 255 2035')
    print('详情4')
    time.sleep(5)
    os.system('adb shell input keyevent 4')
    print('返回')


    time.sleep(5)
    print("完成")


# 从浏览列表开始 横线对齐
def clickEle():
    # 第一个循环
    # 第一个
    # print('进入第一个')
    # os.system('adb shell input tap 949 1033')
    # time.sleep(30)
    # # 返回
    # print('第一个返回')
    # os.system('adb shell input keyevent 4')
    # time.sleep(10)
    # # 领取
    # print('第一个领取')
    # os.system('adb shell input tap 949 1033')
    # time.sleep(10)

    # 第一个
    print('进入第一个')
    os.system('adb shell input tap 949 1033')
    time.sleep(30)
    # 返回
    print('第一个返回')
    os.system('adb shell input keyevent 4')
    time.sleep(10)
    # 领取
    print('第一个领取')
    os.system('adb shell input tap 949 1033')
    time.sleep(10)

    # 第二个
    print('进入第二个')
    os.system('adb shell input tap 949 1251')
    time.sleep(30)
    # 返回
    os.system('adb shell input keyevent 4')
    print('第二个返回')
    time.sleep(10)
    # 领取
    os.system('adb shell input tap 949 1251')
    print('第二个领取')
    time.sleep(10)

    # 第三个
    print('进入第三个')
    os.system('adb shell input tap 949 1465')
    time.sleep(30)
    # 返回
    os.system('adb shell input keyevent 4')
    print('第三个返回')
    time.sleep(10)
    # 领取
    os.system('adb shell input tap 949 1465')
    print('第三个领取')
    time.sleep(10)

    # 第四个
    print('进入第四个')
    os.system('adb shell input tap 949 1683')
    time.sleep(30)
    # 返回
    os.system('adb shell input keyevent 4')
    print('第四个返回')
    time.sleep(10)
    # 领取
    os.system('adb shell input tap 949 1683')
    print('第四个领取')
    time.sleep(10)

    # 第五个
    print('进入第五个')
    os.system('adb shell input tap 949 1920')
    time.sleep(30)
    # 返回
    os.system('adb shell input keyevent 4')
    print('第五个返回')
    time.sleep(10)
    # 领取
    os.system('adb shell input tap 949 1920')
    print('第五个领取')
    time.sleep(10)

    # 第六个
    print('进入第六个')
    os.system('adb shell input tap 949 2148')
    time.sleep(30)
    # 返回
    os.system('adb shell input keyevent 4')
    print('第六个返回')
    time.sleep(10)
    # 领取
    os.system('adb shell input tap 949 2148')
    print('第六个领取')
    time.sleep(10)


# 从第一个图片延边开始 264 * 7 + 348
def clickEleDou():
    count = 0
    while count < 8:
        str1 = 'adb shell input tap 910 ' + str(264 * count + 348)
        print('进入详情')
        os.system(str1)
        time.sleep(30)
        # 返回
        os.system('adb shell input keyevent 4')
        print('返回')
        count = count + 1
        time.sleep(10)

# 惊喜 从上面开始 160 * 5 + 820
def clickJX():
    count = 0
    while count < 6:
        str1 = 'adb shell input tap 910 ' + str(160 * count + 820)
        print('进入详情')
        os.system(str1)
        time.sleep(20)
        # 返回
        os.system('adb shell input keyevent 4')
        print('返回')
        time.sleep(10)
        # 领取
        os.system('adb shell input tap 949 2148')
        print('第领取')
        count = count + 1
        time.sleep(10)

click()
