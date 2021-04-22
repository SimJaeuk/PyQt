import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"
html = requests.get(url).text

soup = BeautifulSoup(html,"html5lib")

tag = soup.select("#assetRealBTC_KRW")[0]
print(tag.text)
tag = soup.select("#assetRealETH_KRW")[0]
print(tag.text)
