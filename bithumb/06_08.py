import pybithumb
import time

con_key = ""
sec_key = ""

bithumb = pybithumb.Bithumb(con_key, sec_key)

order = bithumb.sell_limit_order("BTC",400000000, 1)
print(order)