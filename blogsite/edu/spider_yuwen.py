from selenium import webdriver
# 自动登录
# ~/library/application support/google/chrome
driverOptions = webdriver.ChromeOptions()
driverOptions.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome("chromedriver", 0, driverOptions)
driver.get("http://oldzujuan.21cnjy.com/index.php?mod=frame&do=answer&qid=7932241")