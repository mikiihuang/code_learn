__author__ = 'yumihuang'
# project name:codelearn
# time:2020-04-13


#############selenium测试翻页代码demo############

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
chrome_opt = Options()      # 创建参数设置对象.
# chrome_opt.set_headless()
# chrome_opt.add_argument("--headless")
chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.
driver = webdriver.Chrome(executable_path="/Users/yumi/Desktop/持续学习/codelearn/chromedriver",chrome_options=chrome_opt)
driver.get("https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html")
# more_butoon=driver.find_element_by_class_name("btn-know")
# if more_butoon!=None:
#   more_butoon.click()
# else:
#     pass

html = driver.page_source
html_bs = BeautifulSoup(html,"lxml")
print(html_bs)
button= driver.find_element_by_class_name("moreBtn")
driver.execute_script('arguments[0].scrollIntoView();', button)
time.sleep(5)
# driver.execute_script("arguments[0].click();",button)
# driver.quit()
ActionChains(driver).move_to_element(button).click(button).perform()
# if __name__ == '__main__':
#     pass
