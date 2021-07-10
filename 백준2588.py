a=input()
b=input()

a=int(a)

print(a*int(b[-1]))
print(a*int(b[-2]))
print(a*int(b[-3]))
print(a*int(b))

#int는 123과 같은 수는 subscriptable불가능 (리스트처럼 몇 번째 이딴 게 안됨)