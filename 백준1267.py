n=int(input())
arr= list(map(int, input().split()))
youngsik =0
minsik =0
#통화시간을 30, 60으로 나눈 나머지 + 요금
for i in range(n):
    x=arr[i] //30
    youngsik += 10 * x + 10
    y = arr[i] //60
    minsik += 15 * y + 15

if youngsik == minsik :
    print('Y', 'M', minsik)
elif youngsik > minsik:
    print('M', minsik)
else:
    print('Y', youngsik)
