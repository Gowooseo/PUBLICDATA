import csv

f=open('subwayfee.csv',encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
print(header)
i=1
for row in data:
    print(row)
    if i>5:
        break
    i+=1
f.close()
#----------------------------------------------------------------------
#무임승차 인원이 0인 역 찾기 #1
print('--------------------------------------------------------')
import csv

f=open('subwayfee.csv',encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
rate=0

for row in data:
    for i in range(4,8):
        row[i]=int(row[i]) #4,5,6,7 컬럼 값을 정수로 변환
    rate=row[4]/(row[4]+row[6])
    if row[6]==0:  # 무임승차 인원[6]이 없는 역 출력
        print(row)

f.close()


#-----------------------------------------------------------------------
# 최대 무임 승차 비율 확인
print('------------------------------------------------------------------')
import csv

f=open('subwayfee.csv',encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
max_rate=0
for row in data:
    for i in range(4,8):
        row[i]=int(row[i])
    if row[6]!=0:

        rate=(row[6]*100)/(row[4]+row[6])
        if rate>max_rate:
            max_rate=rate
            print(row,round(rate,2),'%')

f.close()

#최대 유임 승차 인원이 있는 역은?
print('------------------------------------------------------------------')

import csv

f=open('subwayfee.csv',encoding='utf-8-sig')
data=csv.reader(f)
next(data)

max_rate=0
max_row=[]
max_total_num=0

for row in data:
    for i in range(4,8):
        row[i]=int(row[i])
    total_count=row[4]+row[6] #유임승차수+ 무임승차수
    if(row[6]!=0)and (total_count>100000):
        rate=row[4]/total_count
        if rate>max_rate:
            max_rate=rate #가장 큰 것이 나올때까지 반복
            max_row=row   #가장 큰 행이 나올때까지 반복
            max_total_num=total_count  #가장 큰 합이 나올때까지 반복

print()
print( f"호선명:{max_row[1]},역이름:{max_row[3]},전체인원:{max_total_num:,}명,"
       f"유임승차인원:{max_row[4]}명,유임승차 비율:{round(max_rate*100,2):,}%")

#천단위 쉼표를 추가하기 위해 유임승차 비율에 추가


f.close()


#실습:유임 승차 비율이 50% 이하인 역(pie 차트 만들기)
print('------------------------------------------------------------------')


import csv
import matplotlib.pyplot as plt
import platform


f=open('subwayfee.csv',encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
print(header)

# 지금 필요한 것(유임승차 비율, 그중에 50% 이하)
#1) 반복문 사용해서

min_rate=100 #이것보다 더 큰 비율은 없음
min_row=[]   #빈 리스트 담기
min_total_count=0

for row in data:
    for i in range(4,8):
        row[i]=int(row[i])
    total_count=row[4]+row[6]
    if (row[6]!=0) & (total_count>=100000):
        rate=row[4]/total_count
        if rate<=0.5:
            print(row,round(rate,2))
            if rate<=min_rate:
                min_rate=rate
                min_row=row
                min_total_count=total_count

f.close()

# 그래프 그리기

print()
print(f'유임승차비율이 가장 낮은 역')






