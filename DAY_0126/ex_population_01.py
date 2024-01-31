# 대구 산격동 인구 현황

import csv
f=open('age.csv',encoding='utf-8-sig')
data=csv.reader(f)

header=next(data)
print(header)
#row[0] 행정기관
for row in data:
    if '산격3동' in row[0]:
        print(row)
f.close()

#인구수 출력
print('------------------------------------------------------------------------------------')
import csv
f=open('age.csv',encoding='utf-8-sig')
data=csv.reader(f)
result=[]
header=next(data)
print(header)
#row[0] 행정기관
for row in data:
    if '산격3동' in row[0]:#산격3동이 포함된 자료만 출력
        for data in row[3:]: #0~100세 이상까지 자료를 리스트에 추가  row[3]:
            result.append(data)
f.close()


print('------------------------------------------------------------------------------------')
import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f=open('age.csv',encoding='utf-8-sig')
data=csv.reader(f)
result=[]
city=''
header=next(data)
print(header)
#row[0] 행정기관
for row in data:
    if '산격3동' in row[0]:#산격3동이 포함된 자료만 출력
        city=row[0]
        for data in row[3:]:#0~100세 이상까지 자료를 리스트에 추가
            if ',' in data:
                data=data.replace(',','')
            result.append(int(data))  #int(data)를 안해주면 y축에 이상하게 된다.....

f.close()
print(result)

plt.title(f'{city} 인구현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()
print('------------------------------------------------------------------------------------')

# 실습: 인구 구조 그래프 함수 구현

import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

def print_population(population):
    '''
    특정 지역의 인구 현황을 화면에 출력함
    '''
    for i in range(len(population)):
        print(f'{i:3d}세:{population[i]:6d}명',end=' ')
        if (i+1) % 10==0:
            print()

def draw_population(district_name,population_list):
    '''
    특정 지역에 대한 인구 분포를 그래프로 나타냄(plot)
    -district_name:지역 이름
    -population_list:0~100세 이상까지 인구수 리스트
    '''
    # 그래프 출력
    plt.style.use('ggplot')
    plt.title('{} 인구현황'.format(district_name))
    plt.xlabel('나이')
    plt.ylabel('인구수')

    plt.bar(range(101),population_list)
    plt.xticks(range(0,101,10)) #0세 ~100세 이상

    plt.plot(population_list)
    plt.show()

def get_population(city):
    f=open('age.csv',encoding='utf-8-sig')
    data=csv.reader(f)
    next(data) # 헤더 정보 건너뜀

    population_list=[]
    district_name=''
    for row in data:
        if city in row[0]:
            district_name = row[0]
            for data in row[3:]:
                if ',' in data:
                    data=data.replace(',','')
                population_list.append(int(data))
            break  # 처음으로 일치하는 도시명만 검색하기 위함

    f.close()
    print_population(population_list)
    draw_population(district_name,population_list)

city=input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위을 입력하세요:')
get_population(city)