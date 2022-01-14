from selectors import EpollSelector


H=list(input())
N=list(input())
sum =0
for i in range(len(H)-len(N)):
    if H[i,i+len(N)] ==N:
        sum+=1

print(sum)
