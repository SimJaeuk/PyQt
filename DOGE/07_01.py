import pyupbit

df = pyupbit.get_ohlcv("KRW-DOGE")
df.to_excel("DOGE.xlsx")