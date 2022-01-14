#시간초과 오류!!

files=int(input())
File=list(map(int, input().split()))
limit=int(input())

num=0
'''
for i in File:
    if i>0:
        while (i>0):
            num+=1
            i-=limit

print(num*limit)


'''

for i in File :
    if i% limit == 0:
        num += i//limit
    else:
        num += i//limit +1
print(num*limit)

#너무 숫자가 클 수 있을 때는 하나씩 점검하는 것보다 
#나누기한 몫,나머지를 이용해도 좋다.