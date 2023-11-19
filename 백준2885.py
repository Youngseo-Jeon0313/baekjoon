import math

K = int(input())
left = 0; right = 0;
answer = 0

temp_start = 2**int(math.log2(K))
if temp_start ==K:
    print(K,0)

else:
    start = temp_start
    while K>0:
        if K>=start:
            K-=start
        else:
            start//=2
            answer+=1
    print(2*temp_start,answer+1)


'''
test case
1
1 0

2
2 0

3
4 2

5 
8 3

7
8 3

'''