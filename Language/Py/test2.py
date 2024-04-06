import requests
from bs4 import BeautifulSoup

#访问页面并抓取内容
url = 'https://www.geckoterminal.com/eth/pools/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


# print(soup.prettify())
# address = soup.find_all('div', class_='svg.fill-gray-300.hover:fill-gray-100')
# print(address)


div_container = soup.find('div', class_ = 'flex items-center gap-1.5 px-2 py-1')
# for div_child in div_container.find_all('div'):
#     print(div_child)
print(div_container.find_all('div')[0])
    