from pandas import Series 
date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05'] 
xrp_close = [512, 508, 512, 507, 500] 
s = Series(xrp_close, index=date) 
print(s)

print(s[0])
print(s['2018-08-01'])

print(s.index)
print(s.values)


# 인덱스가 화면에 출력되지는 않지만, 내부적으로 자동 설정