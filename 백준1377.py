import sys
input=sys.stdin.readline

N=int(input())
List=[]; 
for i in range(N):
    a=int(input())
    List.append([a,i])
Sort_List=sorted(List)
# print(List)
# print("_____________")
# print(Sort_List)
MAX=0
for i in range(N):
    MAX=max(MAX,Sort_List[i][1]-List[i][1])
'''
위치를 기억하는 방법을
해서 for문을 하나 줄이는 거 말고는
시간초과 해결할 방법이 없음..

'''
print(MAX+1)
# for i in range(N):
    