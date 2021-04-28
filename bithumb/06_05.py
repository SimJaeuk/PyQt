import pybithumb
import time

con_key = ""
sec_key = ""

bithumb = pybithumb.Bithumb(con_key, sec_key)

order = bithumb.buy_market_order("BTC", 1)
print(order)