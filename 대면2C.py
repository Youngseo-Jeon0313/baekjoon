import sys
input=sys.stdin.readline

A,B=map(int,input().split())
A_List=set(map(int,input().split()))
B_List=set(map(int,input().split()))
sumA=len(A_List-B_List)
sumB=len(B_List-A_List)
print(sumA+sumB)