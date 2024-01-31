import csv

def get_minmax_temp(data):
    '''
    최고 기온 및 최고 기온의 날짜 구하기
    '''
    header=next(data)

    min_temp=100  #	최저 기온값을 저장할 변수 초기화(가장 큰 값)
    min_date=''   # 최고 기온의 날짜를 저장할 변수 초기화

    max_temp=-999  #	최고 기온을 저장할 변수 초기화(가장 작은 값)
    max_date=''    #	최고 기온의 날짜를 저장할 변수 초기화

    for row in data:
        if row[3]=='':
            row[3]=100
        row[3]=float(row[3])

        if row[4]=='':#[-1]:리스트에서 마지막 데이터가 없는 경우
            row[4]=-999
        row[4]=float(row[4])
        #	최저 기온 계산
        if row[3] < min_temp:
            min_temp = row[3]
            min_date = row[0]
            #	최고기온 계산
        if row[4] > max_temp:
            max_temp = row[4]
            max_date = row[0]  # 날짜:	index[0]

    print('-'*50)
    print(f'대구 최저 기온 날짜: {min_date},온도:{min_temp}')
    print(f'대구 최고 기온 날짜: {max_date},온도:{max_temp}')

def main():
    f=open('daegu-utf8.csv',encoding='utf-8-sig')
    data=csv.reader(f)
    get_minmax_temp(data)
    f.close()

main()


#데이터를 리스트에 저장하기

import csv
import matplotlib.pyplot as plt
import matplotlib as mp


f=open('daegu-utf8.csv',encoding='utf-8-sig')
data=csv.reader(f)

header=next(data)
result=[]  #빈 리스트 생성

for row in data:
    if row[4] !='': #최고 기온 데이터 값이 있으면,리스트에 저장
        result.append(float(row[4]))

print(len(result))
f.close()
plt.figure(figsize=(10,2)) #그래프 크기 조절(가로 10인치, 세로 2인치)
plt.plot(result,'r') # result 리스트에 저장된 값을 빨간색 그래프로 그려내기
plt.show()  #그래프 그리기



#--------------------------------------------------
#최고 기온 데이터를 히스토그램으로 표현
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import platform

f=open('daegu-utf8.csv',encoding='utf-8-sig')
data=csv.reader(f)
next(data)
result=[]

for row in data:
    if row[-1] !='': #최고 기온을 리스트에 저장
        result.append(float(row[-1]))
f.close()

plt.figure(figsize=(10,	2))
plt.hist(result,bins=500,color='blue') #result에 저장된 값을 히스토 그램으로 그림
plt.rc('font',family='Malgun Gothic')

plt.rcParams['axes.unicode_minus']=False   #레이블에 마이너스('-')기호 깨지는 현상 해결
plt.title("1907년 부터 2023년까지 대구 기온 히스토그램")
plt.show()


# 날짜 정보 분리

'''
문자열 분리:split('구분자')   
'''

date_string1='2024 01 01'
# 공백 기준 분리
print(date_string1.split())

#구분자 기준 분리
date_string2='2024-12-31'
split_date_string=date_string2.split('-')
print(split_date_string)

year=split_date_string[0]
month=split_date_string[1]
day=split_date_string[2]

print(f'연도:{year},	월:{month},	일:{day}')


#----------------------------------------------------------------
# 기온 히스토그램

f=open('daegu-utf8.csv',encoding='utf-8-sig')
data=csv.reader(f)
next(data)
aug=[]

for row in data:
    month=row[0].split('-')[1]  #날짜 정보에서 '-'을 기준으로 분리함
    if row[-1]!='':  #만약 마지막 자료가 공백이라면 이 바로 밑에 split코드를 넣어줘야 함
        if month=='08':
            aug.append(float(row[-1]))  #8월달의 최고기온 정보만 리스트에 추가,
                                        #matplotlib에서 그래프로 표시하기 위해 변환

f.close()

plt.hist(aug,bins=100,color='tomato')
plt.title('대구 8월의 최고 기온 히스토그램')
plt.xlabel("Temperature")  #x축 레이블
plt.ylabel("Counts")       #y축 레이블
plt.show()


#----------------------------------------------------
# 1월과 8월의 기온 데이터 히스토그램

f=open('daegu-utf8.csv',encoding='utf-8-sig')
data=csv.reader(f)
next(data)
aug=[]
jan=[]

for row in data:
    month=row[0].split('-')[1]
    if row[-1]!='':
        if month=='08':
            aug.append(float(row[-1]))
        if month=='01':
            jan.append(float(row[-1]))


f.close()

plt.hist(aug,bins=100,color='tomato',label='Aug')
plt.hist(jan,bins=100,color='b',label='Jan')
plt.title('대구 8월의 최고 기온 히스토그램')
plt.xlabel("Temperature")  #x축 레이블
plt.rc('axes',unicode_minus=False)	#	레이블에 '-'부호가 깨지는 현상 방지
plt.legend()
plt.show()


#-------------------------------------------
# 매년 특정 날짜의 최고 기온 찾기

def draw_graph_on_date(month,day):
    f=open('daegu-utf8.csv',encoding='utf-8-sig')
    data=csv.reader(f)
    next(data)
    result=[]
    for row in data:
        if row[-1]!='':
            date_string=row[0].split('-')
            if date_string[1]==month and date_string[2]==day:
                result.append(float(row[-1])) #

    f.close()
    plt.figure(figsize=(15,2))
    plt.plot(result,'royalblue')
    plt.rc('axes',unicode_minus=False)  #y축에 음수값 표시/
    plt.rc('font',family='Malgun Gothic')
    plt.title(f'매년 {month}월 {day}일 최고 기온 변화')
    plt.show()

month, date=input('날짜(월 일)을 입력하세요: ').split()
draw_graph_on_date(month, date)


#--------------------------------------------------------
#2000년 이후 특정일의 최저,최고 기온 찾기 #2

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import platform

def draw_lowhigh_graph(start_year,month,day):
    f=open('daegu-utf8.csv',encoding='utf-8-sig')
    data=csv.reader(f)
    next(data)
    high_temp=[]
    low_temp=[]
    x_year=[]
    for row in data:
        if row[-1] !='':
            date_string=row[0].split('-')
            if int(date_string[0]) >=start_year:
                if int(date_string[1])==month and int(date_string[2])==day:
                    high_temp.append(float(row[-1]))
                    low_temp.append(float(row[-2]))
                    x_year.append(date_string[0]) # 연도 저장

    f.close()
    plt.figure(figsize=(20,	4))
    plt.plot(x_year, high_temp, 'hotpink', marker='o', label='최고기온')
    plt.plot(x_year, low_temp, 'royalblue', marker='s', label='최저기온')  # 최저 기온 그래프

    if platform.system()=='Windows':
        plt.rc('font', family='Malgun Gothic', size=8)
    else:
        plt.rc('font', family='AppleGothic', size=8)

    plt.rcParams['axes.unicode_minus']=False
    plt.title(f"{start_year}년 이후 {month}월 {day}일의 온도 변화 그래프", size=16)

    plt.legend(loc=2)
    plt.xlabel('year')
    plt.ylabel('temperature')
    plt.show()

draw_lowhigh_graph(2000,	12,	24)

