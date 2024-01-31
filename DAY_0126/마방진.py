# #-----------------------------------------------------------------------
#
# a=[[0]*k for i in range(5)]
# i=0 # 처음 행 위치
# j=2 # 처음 열 위치
# for k in range(1,26):
#     a[i][j]=k
#     if %5==0:
#         i+=1
#     else:
#         i-=1
#         if i<0:
#             i=4
#         j+=1
#         if j>=5:
#             j=0
#
# for i in range(5):
#     for j in range(5):
#         print('{0:5d}'.format(a[i][j]),end='')
#     print()
#
#
# print()


#마방진 만들기

while True:
    n=int(input('마방진 열 개수 입력(홀수만): '))
    if n%2!=1:
        print('짝수 입력 불가')
        continue
    break

square=[[0 for col in range(n)]for row in range(n)]

x=n//2
y=0

for i in range(n**2):
    square[y][x]=i+1
    x1=(x+1)%n
    y1=(y-1)%n
    if square[y1][x1]!=0:  #처음에 0을 주었으므로 0이 바뀌지 않은 초기값이고 , 0이 아니라면 그 값이 바뀐것이므로 값이 들어가 있는것
        y+=1
    else:
        x= x1  #임시 변수 x1으로 지정했다가, 값이 없는 경우 다시 원래 변수에 저장
        y= y1


for i in range(n):
    for j in range(n):
        print(f'{square[i][j]:3}',end='')
    print()