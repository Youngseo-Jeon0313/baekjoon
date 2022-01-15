s = input()
JOI, IOI = 0,0
for i in range(len(s)):
    if s[i:i+3] == 'JOI': JOI += 1
    if s[i:i+3] == 'IOI': IOI += 1
print(JOI)
print(IOI)