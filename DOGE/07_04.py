import pyupbit
 
df = pyupbit.get_ohlcv("KRW-DOGE")
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)
df.to_excel("DOGE3.xlsx")