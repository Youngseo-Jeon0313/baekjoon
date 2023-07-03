T=int(input())
for _ in range(T):
    List=list(input().split())
    start=float(List[0])
    for i in range(1,len(List)):
        if List[i]=='@': start=start*3
        elif List[i]=='%': start=start+5
        else: start=start-7

    print('{:.2f}'.format(start))