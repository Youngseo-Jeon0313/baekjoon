import sys 
input = sys.stdin.readline 
X = int(input()) 
binary_X = bin(X) 
print(binary_X)
print(binary_X.count('1'))
