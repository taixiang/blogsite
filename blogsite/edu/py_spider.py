from selenium import webdriver
import time
from bs4 import BeautifulSoup

driverOptions = webdriver.ChromeOptions()
driverOptions.add_argument(r"user-data-dir=/Users/tx/Library/Caches/Google/Chrome")
driver = webdriver.Chrome("chromedriver", 0, driverOptions)
driver.get("http://oldzujuan.21cnjy.com/index.php?mod=frame&xd=1&xk=2")
time.sleep(3)

ml1 = driver.find_element_by_id("selectTree")
tl = driver.find_element_by_xpath("//div[@class='tList'][1]/ul/li[1]")
print(tl.text)

# driver.find_element_by_class_name("ml1").click()
# time.sleep(5)
# driver.find_element_by_name("QuestType_1").click()
# time.sleep(5)
#
# # 页面元素
# content = BeautifulSoup(driver.page_source, "lxml")
# tList = content.find("div", class_="tList")
# lis = tList.ul.find_all("li")
# for li in lis:
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
#     driver.find_element_by_xpath("./")

