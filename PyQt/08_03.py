import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", interval="minute")
print(df)