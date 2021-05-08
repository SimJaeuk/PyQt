import pyupbit

df = pyupbit.get_ohlcv("KRW-DOGE")
df['range'] = (df['high']-df['low'])* 0.5
df.to_excel("DOGE2.xlsx")