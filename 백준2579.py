'''
think --> 
전전꺼는 상관없음
근데 전꺼는 상관이 너무 있음 ㅠㅠ
아예 생각을 바꿔서 전꺼 말고 전전전꺼 최대값+ 전꺼점수로 구현
'''

D=[]

N=int(input())
arr=[]
for _ in range(N):
    arr.append(int(input()))
D.append(arr[0])
if N==1:
    print(D[-1]);exit()
D.append(max(arr[0]+arr[1],arr[1]))
if N==2:
    print(D[-1]);exit()
D.append(max(arr[0]+arr[2],arr[1]+arr[2]))
#i-3꺼는 상관 없도록 따로 넣어주었음

for j in range(3,N):
    D.append(max(D[j-2],D[j-3]+arr[j-1])+arr[j])

print(D[-1])