N, M = map(int,input().split())
people = list(map(int,input().split()))

answer = 0
people=sorted(people)
left=0; right=len(people)-1
while left<right:
    if people[left]+people[right] < M: left+=1;
    else: answer+=1; left+=1; right-=1;
print(answer)