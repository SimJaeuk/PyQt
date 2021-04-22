#requests
#웹페이지 가져오기

import requests

url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text