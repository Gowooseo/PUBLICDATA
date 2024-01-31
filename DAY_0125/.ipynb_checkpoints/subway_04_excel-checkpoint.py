import pandas as pd
#지하철 시간대별 이용현황

df=pd.read_excel('subway.xls',sheet_name='지하철 시간대별 이용현황',header=[0,1])
print(df.head())

print(df.columns)
print('---------------------------------------------------------------------')
#multi index의 경우,튜플 형식으로 접근
print(df[('호선명','Unnamed: 1_level_1')])
print(df[('지하철역','Unnamed: 3_level_1')])
print('------------------------------------------------------------------------')
commute_time_df=df.iloc[:,[1,3,10,12,14]]
print(commute_time_df.head())

