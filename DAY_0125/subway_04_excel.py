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
print('------------------------------------------------------------------------')
#모든 컬럼의 데이터 타입 확인
print(commute_time_df.dtypes)

#천 단위 콤마 제거
#-apply(lamda x:x.replace(',','')

commute_time_df[('07:00:00~07:59:59','승차')]=commute_time_df[('07:00:00~07:59:59','승차')].apply(lambda x:x.replace(',',''))
commute_time_df[('08:00:00~08:59:59','승차')]=commute_time_df[('08:00:00~08:59:59','승차')].apply(lambda x:x.replace(',',''))
commute_time_df[('09:00:00~09:59:59','승차')]=commute_time_df[('09:00:00~09:59:59','승차')].apply(lambda x:x.replace(',',''))
print('------------------------------------------------')
print(commute_time_df)
print('------------------------------------------------')
#데이터 타입 변경:object에서 int64로 변경
# -df.astype({'컬럼명' : '변경타입'})

commute_time_df=commute_time_df.astype({('07:00:00~07:59:59','승차'):'int64'})
commute_time_df=commute_time_df.astype({('08:00:00~08:59:59','승차'):'int64'})
commute_time_df=commute_time_df.astype({('09:00:00~09:59:59','승차'):'int64'})
print(commute_time_df.dtypes)


print('------------------------------------------------------------')
#각 행(지하철역)의 승차인원 수 합 계산
row_sum_df =commute_time_df.sum(axis=1,	numeric_only=True)
passenger_number_list =	row_sum_df.to_list()
print('$-------------------------------------------------')
print(row_sum_df)
print(passenger_number_list)
print('$-------------------------------------------------')
max_number= row_sum_df.max(axis=0) #해당 열에서 최대값 찾기
print(max_number)

max_index=row_sum_df.idxmax()  #최대값 인덱스
max_line,max_station=df.iloc[max_index,[1,3]]#최대값의 [1]:호선,[3]:지하철역명
print('출근 시간대 최대 승차 인원역:{0} {1} {2:,} 명'.format(max_line,max_station,max_number))  #:,는 천단위 기호 넣어줌
print(df.iloc[max_index,[1,3]])
