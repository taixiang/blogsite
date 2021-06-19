import os
import time
import random


def click():
    count = 0
    while True:
        if count == 20:
            return
        # 淘宝
        os.system('adb shell input tap 537 1165')
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
        # 京东
        os.system('adb shell input tap 875 1695')
        print('详情')
        time.sleep(30)
        # 返回
        os.system('adb shell input keyevent 4')
        print('返回')
        time.sleep(10)
        # 领取
        os.system('adb shell input tap 875 1695')
        print('领取')
        time.sleep(10)
        count += 1
        print(str(count) + "完成")


# 从浏览列表开始 横线对齐
def clickEle():
    count = 0
    # 第一个
    # os.system('adb shell input tap 949 1033')
    # time.sleep(30)
    # # 返回
    # os.system('adb shell input keyevent 4')
    # print('返回')
    # time.sleep(10)
    # # 领取
    # os.system('adb shell input tap 949 1033')
    # print('领取')
    # time.sleep(10)
    #
    # # 第二个
    # os.system('adb shell input tap 949 1251')
    # time.sleep(30)
    # # 返回
    # os.system('adb shell input keyevent 4')
    # print('返回')
    # time.sleep(10)
    # # 领取
    # os.system('adb shell input tap 949 1251')
    # print('领取')
    # time.sleep(10)

    # 第三个
    os.system('adb shell input tap 949 1465')
    time.sleep(30)
    # 返回
    os.system('adb shell input keyevent 4')
    print('返回')
    time.sleep(10)
    # 领取
    os.system('adb shell input tap 949 1465')
    print('领取')
    time.sleep(10)

    # 第四个
    os.system('adb shell input tap 949 1683')
    time.sleep(30)
    # 返回
    os.system('adb shell input keyevent 4')
    print('返回')
    time.sleep(10)
    # 领取
    os.system('adb shell input tap 949 1683')
    print('领取')
    time.sleep(10)

    # 第五个
    os.system('adb shell input tap 949 1920')
    time.sleep(30)
    # 返回
    os.system('adb shell input keyevent 4')
    print('返回')
    time.sleep(10)
    # 领取
    os.system('adb shell input tap 949 1920')
    print('领取')
    time.sleep(10)

    # 第六个
    os.system('adb shell input tap 949 2148')
    time.sleep(30)
    # 返回
    os.system('adb shell input keyevent 4')
    print('返回')
    time.sleep(10)
    # 领取
    os.system('adb shell input tap 949 2148')
    print('领取')
    time.sleep(10)


clickEle()
