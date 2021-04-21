import pyupbit

price = pyupbit.get_current_price("KRW-XRP")
print("현재 리플의 가격은 ",price, "입니다.")
price2 = pyupbit.get_current_price("KRW-BTC")
print("현재 비트코인의 가격은 ",price2, "입니다.")

price = pyupbit.get_current_price(["KRW-BTC","KRW-XRP"])
print(price)