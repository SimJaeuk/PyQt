import pybithumb
import time

con_key = ""
sec_key = ""

bithumb = pybithumb.Bithumb(con_key, sec_key)

order = bithumb.buy_limit_order("BTC", 4000100, 0.001)
print(order)
