# 모든 역의 유임,무임,승하차 분석
import csv
max=[0]*4
max_station=['']*4
label=['유임승차','유임하차','무임승차','무임하차']

#with 구문: 자동으로 파일을 close()시킴
with open('subwayfee.csv',encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)

    for row in data:
        for i in range(4,8):
            row[i]=int(row[i])
            if row[i]>max[i-4]: #원본데이터의 컬럼(인덱스-4) ->max리스트의 인덱스
                max[i-4]=row[i]
                max_station[i-4]=row[3]+' '+ row[1] #역이름 지하철 노선 추가


for i in range(4):
    print(f'{label[i]}:{max_station[i]} {max[i]:,}명')




# 전체 지하철역 승하차 인원 분석 및 저장

#파일 저장:savefig('파일 이름',dpi)
print('-----------------------------------------------------------------')
import csv
import matplotlib.pyplot as plt
import platform

label=['유임승차','유임하차','무임승차','무임하차']
color_list=['#ff9999','#ffc000','#8fd9b6','#d395d0'] #파이 차트 컬러 값
pic_count=0
with open('subwayfee.csv',encoding='utf-8-sig') as f:
    data =csv.reader(f)
    next(data)

    if (platform.system()=='Windows'):
        plt.rc('font',family='Malgun Gothic')

    else:
        plt.rc('font',family='AppleGothic')

    for row in data:
        for i in range(4,8):
            row [i]=int(row[i])
        print(row)
        plt.figure(dpi=100) #저장할 그림파일의 dpi 설정
        plt.title(row[3]+' '+row[1])
        plt.pie(row[4:8],labels=label,colors=color_list,autopct='%.1f%%',shadow=True)
        plt.savefig('img/'+row[3]+' '+row[1]+'.png')
        plt.close() #파일 닫기

        pic_count+=1
        if pic_count>=10:
            break
