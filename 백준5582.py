'''
DP 편집거리 
'''
S1 = input()
S2 = input()

DP=[[0 for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]
for i in range(len(S1)):
    for j in range(len(S2)):
        if S1[i]==S2[j]:
            DP[i+1][j+1]=DP[i][j]+1
answer = 0    
for i in range(len(S1)+1):
    answer = max(answer, max(DP[i]))

print(answer)