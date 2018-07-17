from selenium import webdriver
import time
from bs4 import BeautifulSoup

driverOptions = webdriver.ChromeOptions()
driverOptions.add_argument(r"user-data-dir=/Users/tx/Library/Caches/Google/Chrome")
driver = webdriver.Chrome("chromedriver", 0, driverOptions)
driver.get("http://oldzujuan.21cnjy.com/index.php?mod=frame&xd=1&xk=2")
# 获取当前窗口句柄（窗口A）
handle = driver.current_window_handle
time.sleep(3)

ml1 = driver.find_element_by_id("selectTree")
tl = driver.find_element_by_xpath("//div[@class='tList'][1]/ul/li[1]/div[3]/a[2]").click()
time.sleep(3)
# 获取当前所有窗口句柄（窗口A、B）
handles = driver.window_handles
# 对窗口进行遍历
for newhandle in handles:
  # 筛选新打开的窗口B
  if newhandle!=handle:
    # 切换到新打开的窗口B
    driver.switch_to.window(newhandle)

parse_content = BeautifulSoup(driver.page_source, "lxml")
lanmu = parse_content.find_all("div",class_="lanmu")
for lan in lanmu:
    text = lan.getText()
    txt = text[3:].strip()
    print(txt)

# 关闭当前窗口B
driver.close()
#切换回窗口A
driver.switch_to.window(handles[0])

driver.find_element_by_css_selector("[title='转到第2页']").click()


# driver.find_element_by_class_name("ml1").click()
# time.sleep(5)
# driver.find_element_by_name("QuestType_1").click()
# time.sleep(5)
#
# # 当前页码
# cur_num = 0
#
# # 页面元素
# content = BeautifulSoup(driver.page_source, "lxml")
# tList = content.find("div", class_="tList")
# lis = tList.ul.find_all("li")
# for i, li in enumerate(lis):
#     ques_content = li.find("div", attrs={"name": "QusetContent"})
#     # 题目
#     div_title = ques_content.find("div", class_="Q-title")
#     [s.extract() for s in div_title("span")]
#     title = div_title.getText().strip()
#     print(title)
#
#     # 选项
#     div_selector = ques_content.find("div", class_="Q-selectors")
#     tds = div_selector.tbody.tr.find_all("td")
#     for td in tds:
#         sel = td.getText()
#         print(sel)
#
#     # 解析
#     q_parse = li.find("div", class_="Q-parse")
#     path = "//div[@class='tList'][1]/ul/li[%d]/div[3]/a[2]" % (i + 1)
#     parse = driver.find_element_by_xpath(path).click()
#     time.sleep(2)
#     # 获取当前所有窗口句柄（窗口A、B）
#     handles = driver.window_handles
#     # 对窗口进行遍历
#     for newhandle in handles:
#         # 筛选新打开的窗口B
#         if newhandle != handle:
#             # 切换到新打开的窗口B
#             driver.switch_to.window(newhandle)
#
#     parse_content = BeautifulSoup(driver.page_source, "lxml")
#     lanmu = parse_content.find_all("div", class_="lanmu")
#     for i, lan in enumerate(lanmu):
#         text = lan.getText()
#         txt = text[3:].strip()
#         print(txt)
#
#     # 关闭当前窗口B
#     driver.close()
#     # 切换回窗口A
#     driver.switch_to.window(handles[0])
#
#     # 下一页


