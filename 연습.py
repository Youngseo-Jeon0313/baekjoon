import sys

s = ''
for line in sys.stdin:
    s += line.rstrip()
arr = list(map(int, s.split(',')))
print(sum(arr))


# import sys
# input = sys.stdin.read

# print(sum(map(int,input().replace('\n','').split(','))))