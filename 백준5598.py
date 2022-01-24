arr = list(input())
for i in range(len(arr)):
    arr[i] = chr(((ord(arr[i]) - 42) % 26) + 65)
print(''.join(arr))