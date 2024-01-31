import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f=open('gender.csv',encoding='utf-8-sig')
data=csv.reader(f)
population=[]  #pie chart에 넣을 데이터(남,여 인구수)
city=input('찾고 싶은 지역의 이름을 입력하세요:')
male_count=0
female_count=0

for row in data:
    if city in row[0]:
        male_count=int(row[104].replace(',',''))# 자리수 문자열 제거 및 숫자로 변환
        female_count=int(row[207].replace(',',''))
        break

print(f'{city} 남자 인구수: {male_count:,}명,여자 인구수:{female_count:,}명')

population=[male_count,female_count]
color=['cornflowerblue','tomato']
plt.pie(population,labels=['남','여'],autopct='%.1f%%',colors=color,startangle=90)
plt.title(city + " 남녀 성별 비율")
plt.show()

# 서울특별시 및 5대 광역시 연령대별 남녀 인구수 비교
