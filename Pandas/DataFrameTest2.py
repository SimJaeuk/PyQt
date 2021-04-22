import pandas as pd 

url = "https://finance.naver.com/item/sise_day.nhn?code=066570" 

df = pd.read_html(url) 
print(df[0])

#네이버 증권 일별 시세의 웹페이지가 변경되어 현재는 안됨