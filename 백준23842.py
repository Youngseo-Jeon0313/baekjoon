NUM=[6,2,5,5,4,5,6,4,7,6,2,2]
#    1 2 3 4 5 6 7 8 9 0 + =

N=int(input())

for i in range(100):
    for j in range(i,100-i):
        ans=i+j
        if NUM[i%10]+NUM[i//10]+NUM[j%10]+NUM[j//10]+2+2+NUM[ans//10]+NUM[ans%10]==N:
            i=str(i).zfill(2)
            j=str(j).zfill(2)
            ans=str(ans).zfill(2)
            print(i,'+',j,'=',ans,sep='')
            exit()

print('impossible')