T=int(input())
for _ in range(T):
    h,w,n=map(int,input().split())
    front = (n%h)
    if n%h==0: front = h;  back = n//h
    else: back=n//h+1
    print(front*100+back)