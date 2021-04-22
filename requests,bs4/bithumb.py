import requests
from bs4 import BeautifulSoup
 
def get_per(code):
    url = "http://www.bithumb.com/"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#assetRealBTC_KRW")
    tag = tags[0]
    return (tag.text)

print(get_per(""))
