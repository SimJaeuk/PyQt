import pybithumb
import time

while 1:
    price = pybithumb.get_current_price("BTC")
    print(price)
    time.sleep(0.2)