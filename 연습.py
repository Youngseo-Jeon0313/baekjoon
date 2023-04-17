n = int(input())
arr = list(map(int, input().split()))
youngsik = 0
minsik = 0
for i in range(n):
    #영식 요금제
    x = arr[i] // 30
    youngsik += 10 * x + 10
    #민식 요금제
    y = arr[i] // 60
    minsik += 15 * y + 15

if youngsik == minsik:
    print('Y','M',minsik)
elif youngsik > minsik: #민식 요금제가 더 쌈
    print('M',minsik)
else: #영식 요금제가 더 쌈
    print('Y',youngsik)