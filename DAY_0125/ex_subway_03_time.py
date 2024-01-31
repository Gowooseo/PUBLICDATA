#새벽 4시 지하철 이용인원 전체

import csv

result=[]
total_number=0
with open('subwaytime.csv',encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)  #2줄의 헤더 정보 건너뜀
    next(data)
    for row in data:
        row[4:]=map(int,row[4:])
        total_number+=row[4]
        result.append(row[4])

print(f'총 지하철 역의 수: {len(result)}') #len()안에든 리스트의 개수
print(f'새벽 4시 승차 인원:{total_number:,}')


print('---------------------------------------------------------------------')

# 새벽 4시 지하철 이용 인원 그래프

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('subwaytime.csv',encoding='utf-8-sig')as f:
    data=csv.reader(f)
    next(data)
    next(data)
    result=[]   #bar차트를 그려야하기 때문에 리스트를 추가
    total_number=0
    max_num=-1
    max_station=''

    for row in data:
        row[4:]=map(int,row[4:])
        total_number+=row[4]
        result.append(row[4])  #bar차트를 그려야 하기떄문에 리스트를 추가
        if row[4]>max_num:
            max_num=row[4]
            max_station=row[3]

print('새벽 4시 승차 인원수:{0:,}'.format(total_number))
print('최대 승차역:{0},인원수:{1:,}'.format(max_station,max_num))
result.sort()  #오름차순 정렬
plt.figure(dpi=100)
plt.bar(range(len(result)),result)
plt.title('새벽 4시 지하철 승차인원 현황')
plt.show()

print('---------------------------------------------------------------------')
#-------------------------------------------------------------
#출근 시간대 지하철 이용 현황#1

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('subwaytime.csv',encoding='utf-8-sig')as f:
    data=csv.reader(f)
    next(data)
    next(data)
    result=[]
    total_number=0
    max_num=-1
    max_station=''

    for row in data:
        row[4:]=map(int,row[4:])
        row_sum=sum(row[10:15:2])  #오전 7시,8시,시 승차(row[10]+row[12]+row[14])

        result.append(row_sum)
        if row_sum>=max_num:
            max_num=row_sum
            max_station=row[3]+'('+row[1]+')'

print(f'최대 승차 인원역:{max_station}{max_num:,}')
result.sort(reverse=True)

#1행 ,2열의 그래프
plt.figure(figsize=(10,4))
ax1=plt.subplot(1,2,1) #행의 수,열의 수, 인덱스
plt.title('10개 역의 승차 인원수',size=12)
plt.bar(range(len(result)),result)

plt.suptitle('출근시간대 승차 인원 현황\n',size=20)
plt.tight_layout()
plt.show()

#시간대별 가장 많이 승차하는 역 정보 분석

import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

with open('subwaytime.csv',encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)
    next(data)
    max=[0]*23
    max_station=['']*23
    xtick_list=[]
    for i in range(4,27):
        n=i%24
        xtick_list.append(str(n))

    for row in data:
        row[4:]=map(int,row[4:])
        for j in range(23):
            a=row[j*2+4] #j=0:data[0*2+4]의 값을 max[0]에 저장하기 위함
            if a>max[j]:
                max[j]=a
                max_station[j]=xtick_list[j]+'시:'+row[3] #4시:구로

for i in range(len(max)):
    print(f'{max_station}:{max[i]:,}')


if platform.system()=='Windows':
    plt.rc('font',family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')

plt.figure(figsize=(10,10))
plt.title('시간대별 최대 승차역 정보')
plt.bar(range(23),max)
plt.xticks(range(23),labels=max_station,rotation=80)
plt.tight_layout()
plt.show()

print('---------------------------------------------------------------------')
# 모든 지하철 역에서 시간대별 지하철 인원
import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

with open('subwaytime.csv',encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)
    next(data)
    subway_in=[0]*24  #승차인원 저장 리스트
    subway_out=[0]*24 #하차인원 저장 리스트

    for row in data:
        row[4:]=map(int,row[4:])
        for i in range(24):
            subway_in[i]+=row[i*2+4]
            subway_out[i]+=row[i*2+5]

        if platform.system()=='Windows':
            plt.rc('font',family='Malgun Gothic')
        else:
            plt.rc('font','AppleGothic')

xtick_list=[]
for i in range(4,28):
    n=i%24
    xtick_list.append(str(n))

plt.figure(dpi=100)
plt.title('지하철 시간대별 승하차 인원 추이',size=16)
plt.grid(linestyle=':') #그리드 라인 표시
plt.plot(subway_in,label='승차')
plt.plot(subway_out, label='하차')
plt.legend()

plt.xticks(range(24),labels=xtick_list)
plt.xlabel('시간')
plt.ylabel('인원(천만명)')
plt.show()


#lamda와 operator를 이용한 정렬

#(1) lamda
import operator

names={'Mary':10999,'Sams':2111,'Aimy':9778,'Tom':20245,'Michale':27115,'Kelly':7855}

#Key를 기준으로 정렬(기본:오름차순)
print("[lambda]dict 정렬:key 기준 오름차순")
res=sorted(names.items(),key=(lambda x:x[0]))
print(res)
print()

#Value를 기준으로 정렬(기본:내림차순)
print("[lambda]dict 정렬:Value 기준 내림차순")
res=sorted(names.items(),key=(lambda x:x[1]),reverse=True)
print(res)

#(2) operator 기준

names={'Mary':10999,'Sams':2111,'Aimy':9778,'Tom':20245,'Michale':27115,'Kelly':7855}

#Key를 기준으로 정렬(기본:오름차순)
sorted_x =sorted(names.items(),	key=operator.itemgetter(0))
print("[operator]	dict정렬:	key	기준,	오름차순")
print(sorted_x)
#Value를 기준으로 정렬(기본:내림차순)
sorted_x =sorted(names.items(),	key=operator.itemgetter(1),reverse=True)
print("[operator]	dict정렬:	Value	기준,	내림차순")
print(sorted_x)

