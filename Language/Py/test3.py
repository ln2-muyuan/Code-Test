from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


# 打开网页，等待加载完成
url = 'https://freegpt.one/'
browser = webdriver.Edge()
browser.get(url)
wait = WebDriverWait(browser, 10)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.RNmpXc')))

# 点击按钮，等待页面加载完成
button.click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.result')))

# # 使用 BeautifulSoup 从页面中提取内容
# page_source = browser.page_source
# soup = BeautifulSoup(page_source, 'html.parser')
# results = soup.select('div.result')

# # 在控制台上打印结果
# for result in results:
#     print(result.text)