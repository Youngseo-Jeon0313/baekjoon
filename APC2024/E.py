N = int(input())

# 만들 수 있는 daldidalgo 갯수
D_num = 0
answer = 0
# 첫번째 
answer+=8
D_num+=1

while N:
    #print(N, D_num, answer)
    N-=min(D_num, N)
    D_num+=min(D_num, N); answer+=1
    

#남은 n 더해줌
answer+=1
print(answer)