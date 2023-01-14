import sys
input = sys.stdin.readline

X_1 = int(input())
Y_basic = int(input())
Y_limit = int(input())
Y_surcharge_for_1L = int(input())

P=int(input())

X=X_1 * P
if(Y_limit>P) : Y = Y_basic
else: Y = Y_basic + Y_surcharge_for_1L*(P-Y_limit) 

print(min(X,Y))