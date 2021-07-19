#파이썬에서 변수 생성
#setarr() 함수 사용
#setarr(object, name, value)


num_list=[]

for i in range(3):
    num_list.append(int(input()))

x=1
for i in range(3):
    x*=num_list[i]


for i in range(10):
    y=0
    for j in str(x):
        if j==i:
            y+=1
    print(y)
