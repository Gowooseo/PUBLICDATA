import csv
#--------------------------------------------------
#순서
#1) csv 모듈을 불러옴(import csv)
#2) 파일 =open('파일이름',mode='r',encoding=None)
#3) csv reader 객체 생성 및 파일 읽어 오기
#4) 읽은 데이터(data 변수) 출력
#5) 파일 close

f=open('daegu.csv','r',encoding='utf-8')  #mode=w 쓰기 용도,'euc.kr' 한글 사용=>'ep949'
data=csv.reader(f, delimiter=',')
print(data) #csv_reader 객n
# 체 출력
f.close() # 파일닫기

#----------------------------------------
import csv

f=open('daegu.csv','r',encoding='utf-8') #daegu.csv 파일 전체에 대한 객체 => 1라인씩 읽어옴
data=csv.reader(f,delimiter=',') #delimiter는 반드시 한 스트링 가짐, 띄워쓰기 해서 틀림
count=0
for row in data:
    if count>5:
        break
    else:
        print(row) #1 라인 출력
    count +=1
f.close()

#encoding='utf-8-sig' 정의 및 '\t' 삭제
#-----------------------------------------------------------------------
import csv
#encoding='utf-8-sig'로 '\ufeff' 제거
fin=open('daegu.csv','r',encoding='utf-8-sig')  #fin파일 읽기
data=csv.reader(fin,delimiter=',')

#newline='':한 라인씩 건너 뛰며 저장되는 현상 없앰
fout=open('daegu-utf8.csv','w',newline='',encoding='utf-8-sig')  # fout라는 원래 없던게 생김
wr=csv.writer(fout)

for row in data:
    for i in range(len(row)):
        row[i]=row[i].replace('\t','') #\t를 제거
    print(row)
    wr.writerow(row)  #writerow(row): 한 행씩 파일로 저장

fin.close()
fout.close()
print('파일 저장 완료')



#데이터 헤더 출력하기
#-next()함수=>
# 첫번쨰 데이터 행을 읽어오면서 데이터의 탐색 위치를 다음행으로

import csv
f=open('daegu-utf8.csv',encoding='utf-8-sig')  #utf-8-sig로 변환한 파일도 encoding='utf-8-sig적용

data=csv.reader(f,delimiter=',')
header=next(data)   #next(data) data는 두번쨰 줄을 가리킴
print(header) #헤더 문자열 출력

i=1
for row in data: # 실제 기온정보를 가지고 있음
    print(row)
    if i>=5:
        break #5개의 데이터를 출력하면 break
    i+=1
f.close()


# 대구가 가장 더웠던 날과 가장 추웠던 날의 온도 및 날짜?
