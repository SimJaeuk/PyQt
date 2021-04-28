import pybithumb
import time

con_key = ""
sec_key = ""

bithumb = pybithumb.Bithumb(con_key, sec_key)

for ticker in pybithumb.get_tickers() :
    balance = bithumb.get_balance(ticker)
    print(ticker, ":", balance)
    time.sleep(0.1)