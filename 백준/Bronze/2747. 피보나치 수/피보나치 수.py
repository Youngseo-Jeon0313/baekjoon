f=[0,1,1]
for i in range(43):
    f.append(f[-1]+f[-2])
n=int(input())
print(f[n])