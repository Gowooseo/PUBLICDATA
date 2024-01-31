import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f=open('gender.csv',encoding='utf-8-sig')
data=csv.reader(f)


header=next(data)
Gu_list=['대구광역시','대구광역시 중구', '대구광역시 동구', '대구광역시 서구',
         '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구',
         '대구광역시 달서구', '대구광역시 달성군']

male_count=[]
female_count=[]

for row in data:
    for gu in Gu_list:
        if gu in row[0]:
            male_count.append(int(row[104].replace(',','')))
            female_count.append(int(row[207].replace(',', '')))
            break


plt.figure(figsize=(10,10))
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.pie([male_count[i],female_count[i]],labels=['남성','여성'],autopct='%.1f%%',startangle=90)
    plt.title(Gu_list[i])

plt.suptitle('대구광역시 구별 남녀 인구 비율')
plt.show()

