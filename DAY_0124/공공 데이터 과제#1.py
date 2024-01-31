# 과거 10년 동안의 대구 날씨 데이터에서 1년 중 일교차가 가장 큰 달은 각각 몇 월인지 그래프로 표시

#기간: 최근 10년(2014년 ~2023년)
#- 각 달의 일교차(최고기온-최저기온)를 비교하여 각 년도별 일교차가 가장 큰 달을 bar 그래프로 표시
#-Pandas 또는 Python 코딩

#데이터 분석

#필요한 것= 최근 10년의 기간,각 달의 일교차(최고기온-최저기온),각 년도별 일교차가 가장 큰 달 구하기
           #bar 그래프로 만들기
import	csv
import	matplotlib.pyplot as	plt
import	platform
import koreanize_matplotlib
import pandas as pd

#일교차 찾고=> 평균 구하고=> 12달 중에서 최대값 찾고=> 반복문 10번
# 파일 불러오고 '날짜' 컬럼 datetime 타입으로 변형
weather_df =pd.read_csv('daegu-utf8-df.csv',	encoding='utf-8-sig')
weather_df['날짜']=pd.to_datetime(weather_df['날짜'],format='%Y-%m-%d')

weather_df['일교차']=weather_df['최고기온']-weather_df['최저기온']  # 일교차 컬럼 만들기

# print(weather2014['최고기온'])
# print(weather2014['최고기온']-weather2014['최저기온'])
#
# print(weather2014['일교차'])

tem_ram_max_list = []

for y in range(2014,2024):
    high_max = -9999
    month_max = 0
    yearDF = weather_df[weather_df['날짜'].dt.year==y]
    for m in range(1,13):
        ymDF = yearDF[yearDF['날짜'].dt.month == m]
        tem_ram = ymDF['일교차'].mean()
        if tem_ram > high_max:
           high_max = tem_ram #가장 큰 값이 나올때까지 반복
           month_max = m      #가장 큰 값이 나올때까지 반복
        # tem_ram_list.append(ymDF['일교차'].mean())
    tem_ram_max_list.append((y, month_max, round(high_max,1)))

plt.bar([ i[0] for i in tem_ram_max_list ] ,[ i[-1] for i in tem_ram_max_list ])
plt.title("지난 10년간 대구의 일교차가 가장 큰 달")
plt.xlabel("year/month")
plt.ylabel("일교차")
plt.show()


# for y in range(2014,2024):
#     for m in range(1,13):
#         ymDF = weather_df[(weather_df['날짜'].dt.month == m) & (weather_df['날짜'].dt.year==y)]

print(tem_ram_max_list)




#2.

# def main():
# search_month=int(input("달을 입력하세요: "))


start=int(input('시작 연도를 입력하세요:'))
end=int(input('마지막 연도를 입력하세요:'))
month_weather=int(input('기온 변화를 측정할 달을 입력하세요:'))


weather_df=	pd.read_csv('daegu-utf8-df.csv',	encoding='utf-8-sig')
weather_df['날짜']=pd.to_datetime(weather_df['날짜'],format='%Y-%m-%d')

max_list=[0]*(end-start)
min_list=[0]*(end-start)

for year in range(end-start):
    max_tem_df=weather_df[(weather_df['날짜'].dt.year==start+year) & (weather_df['날짜'].dt.month==month_weather)]
    max_list[year]= round(max_tem_df['최고기온'].mean(),1)

    min_tem_df = weather_df[(weather_df['날짜'].dt.year == start + year) & (weather_df['날짜'].dt.month == month_weather)]
    min_list[year] = round(min_tem_df['최저기온'].mean(), 1)

print(f'{start}년부터  {end}년까지 {month_weather}월의 기온변화 ')
print(f'{month_weather} 월 최저기온 평균:')
# for a in min_list:
#     print(a, end='')
print(', '.join(map(str, min_list)))
print(f'{month_weather} 월 최고기온 평균:')
print(', '.join(map(str, max_list)))
# print(str(min_list[1:-1]))


plt.rcParams['axes.unicode_minus']	=	False
plt.figure(figsize=(10,	4))
plt.plot(range(start, end),max_list	,	marker='s',	markersize=6,	color='b'	)
plt.plot(range(start, end),min_list	,	marker='s',	markersize=6,	color='r'	)
# plt.title(title)
plt.legend(['최고기온', '최저기온'],loc=2)
plt.show()










