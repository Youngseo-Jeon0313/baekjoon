def print_hanoi(start,mid,end,disc):
    if disc>=1:
        print_hanoi(start,end,mid,disc-1)
        print(start,end)
        print_hanoi(mid,start,end,disc-1)

N=int(input())
print(2**N-1)
if N<=20:
    print_hanoi(1,2,3,N)