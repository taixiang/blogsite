from selenium import webdriver
import time
from bs4 import BeautifulSoup
import xlsxwriter

driverOptions = webdriver.ChromeOptions()
# C:\Users\Administrator\AppData\Local\Google\Chrome\User Data   /Users/tx/Library/Caches/Google/Chrome
driverOptions.add_argument(r"user-data-dir=/Users/tx/Library/Caches/Google/Chrome")
driver = webdriver.Chrome("chromedriver", 0, driverOptions)
driver.get("http://oldzujuan.21cnjy.com/index.php?mod=frame&xd=1&xk=2")
# 获取当前窗口句柄（窗口A）
handle = driver.current_window_handle
time.sleep(3)

# ml1 = driver.find_element_by_id("selectTree")
# tl = driver.find_element_by_xpath("//div[@class='tList'][1]/ul/li[1]/div[3]/a[2]").click()
# time.sleep(3)
# # 获取当前所有窗口句柄（窗口A、B）
# handles = driver.window_handles
# # 对窗口进行遍历
# for newhandle in handles:
#   # 筛选新打开的窗口B
#   if newhandle!=handle:
#     # 切换到新打开的窗口B
#     driver.switch_to.window(newhandle)
#
# parse_content = BeautifulSoup(driver.page_source, "lxml")
# lanmu = parse_content.find_all("div",class_="lanmu")
# for lan in lanmu:
#     text = lan.getText()
#     txt = text[3:].strip()
#     print(txt)
#
# # 关闭当前窗口B
# driver.close()
# #切换回窗口A
# driver.switch_to.window(handles[0])
#
# driver.find_element_by_css_selector("[title='转到第2页']").click()


driver.find_element_by_class_name("ml1").click()
time.sleep(5)
# driver.find_element_by_css_selector("[treeid='18488']").click()
# time.sleep(5)
driver.find_element_by_name("QuestType_1").click()
time.sleep(5)

# 当前页码
cur_num = 58

for i in range(10):
    page = "[title='转到第%d页']" % (9 + 5 * i)
    driver.find_element_by_css_selector(page).click()
    time.sleep(10)

# page = "[title='转到第%d页']" % 9
# driver.find_element_by_css_selector(page).click()
# time.sleep(2)
#
# page2 = "[title='转到第%d页']" % 14
# driver.find_element_by_css_selector(page2).click()
# time.sleep(2)
#
# page2 = "[title='转到第%d页']" % 19
# driver.find_element_by_css_selector(page2).click()
# time.sleep(2)
#
# page2 = "[title='转到第%d页']" % 24
# driver.find_element_by_css_selector(page2).click()
# time.sleep(2)
#
# page2 = "[title='转到第%d页']" % 29
# driver.find_element_by_css_selector(page2).click()
# time.sleep(2)
#
# page2 = "[title='转到第%d页']" % 34
# driver.find_element_by_css_selector(page2).click()
# time.sleep(2)

# page3 = "[title='转到第%d页']" % cur_num
# driver.find_element_by_css_selector(page3).click()
# time.sleep(10)

# 记录空题目
file_empty = open('empty.txt', 'a', encoding='utf-8')

# 创建excel表格
file = xlsxwriter.Workbook("yuwen6.xlsx")
# 创建工作表
sheet = file.add_worksheet()
headers = ["题目", "A", "B", "C", "D", "考点", "正确答案", "分析"]
# 写表头
for head_i, header in enumerate(headers):
    # 第一行为表头
    sheet.write(0, head_i, header)
sheet.set_column(0, 0, 44)
sheet.set_column(1, 1, 24)
sheet.set_column(2, 2, 24)
sheet.set_column(3, 3, 24)
sheet.set_column(4, 4, 24)
sheet.set_column(5, 5, 24)
sheet.set_column(7, 7, 34)

try:
    while True:

        if cur_num == 421:
            break

        # 页面元素
        content = BeautifulSoup(driver.page_source, "lxml")
        tList = content.find("div", class_="tList")
        lis = tList.ul.find_all("li")
        # 一页的数据
        for i, li in enumerate(lis):
            print("==========================================")
            print("当前第%d页" % cur_num)
            print("==========================================")
            print("当前第%d题" % (i + 1))
            print("==========================================")
            ques_content = li.find("div", attrs={"name": "QusetContent"})
            # 题目
            div_title = ques_content.find("div", class_="Q-title")
            [s.extract() for s in div_title("span")]
            title = div_title.getText().strip()
            print("题目-----------------------------------")
            print(title)

            # 选项
            div_selector = ques_content.find("div", class_="Q-selectors")
            if div_selector is None:
                continue
            other_sel = div_selector.find("div", class_="Q-selectors")
            if other_sel is not None:
                print("多余的题目====================")
                continue
            tds = div_selector.table.tbody.find_all("td")
            print("选项-----------------------------------")
            opts = [""] * 4
            for td_i, td in enumerate(tds):
                sel = td.getText()
                opts[td_i] = sel
                print(sel)

            # 解析
            q_parse = li.find("div", class_="Q-parse")
            path = "//div[@class='tList'][1]/ul/li[%d]/div[3]/a[2]" % (i + 1)
            parse = driver.find_element_by_xpath(path).click()
            time.sleep(2)
            # 获取当前所有窗口句柄（窗口A、B）
            handles = driver.window_handles
            # 对窗口进行遍历
            for newhandle in handles:
                # 筛选新打开的窗口B
                if newhandle != handle:
                    # 切换到新打开的窗口B
                    driver.switch_to.window(newhandle)

            parse_content = BeautifulSoup(driver.page_source, "lxml")
            lanmu = parse_content.find_all("div", class_="lanmu")
            print("解析----------------------------------")
            parse_list = [""] * 3
            for j, lan in enumerate(lanmu):
                text = lan.getText()
                txt = text[3:].strip()
                parse_list[j] = txt
                print(txt)

            row = (i + 1) + (cur_num - 1) * 10
            # 没有答案的备注
            if len(parse_list[1]) <= 0:
                file_empty.write(str(cur_num) + "页，" + str(i + 1) + "题 " + "\n")
            # 设置行高
            sheet.set_row(row, 20)

            sheet.write(row, 0, title)
            sheet.write(row, 1, opts[0])
            sheet.write(row, 2, opts[1])
            sheet.write(row, 3, opts[2])
            sheet.write(row, 4, opts[3])
            sheet.write(row, 5, parse_list[0])
            sheet.write(row, 6, parse_list[1])
            sheet.write(row, 7, parse_list[2])

            # 关闭当前窗口B
            driver.close()
            # 切换回窗口A
            driver.switch_to.window(handles[0])

        # 下一页
        cur_num += 1
        page = "[title='转到第%d页']" % cur_num
        driver.find_element_by_css_selector(page).click()
        time.sleep(10)

        # # 关闭表格
        # file.close()
except:
    file.close()

# 关闭表格
file.close()
