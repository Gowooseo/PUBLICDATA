#--------------------------------------------------
# 1. 대구광역시 전체 및 8개 구,군별 (중구, 동구, 서구, 남구, 북구, 수성구, 달서구, 달성군)
# 남녀 비율을 각각의 파이 차트로 구현하세요. (hw03.py)
# - subplots를 이용하여 3x3 형태의 총 9개의 subplot을 파이 차트로 구현
#gender.csv 파일 사용













f=open('gender.csv',encoding='utf-8-sig')
data=csv.reader(f)
population=[]
Gu_list=['대구광역시','대구광역시 중구', '대구광역시 동구', '대구광역시 서구',
         '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구',
         '대구광역시 달서구', '대구광역시 달성군']
male_count=0
female_count=0
# 남 인구수 인덱스 : 104 / 여 인구수 인덱스가 207

man_list = []
woman_list = []

plt.figure(figsize=(10,10))
for row in data:
    for gu in Gu_list:
        if gu in row[0]:
            man_list.append(int(row[104].replace(',','')))
            woman_list.append(int(row[207].replace(',','')))
            break

print(man_list)
print(woman_list)

for i in range(1, 10):
    plt.subplot(3, 3, i)
    plt.pie([man_list[i-1], woman_list[i-1]], labels=['남성', '여성'], autopct='%.1f%%', startangle=90,textprops={'fontsize':'large'})
    plt.title(Gu_list[i-1])

plt.suptitle('대구광역시 구별 남녀 인구 비율')
plt.show()












