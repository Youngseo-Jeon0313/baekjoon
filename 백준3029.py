h1,m1,s1=map(int, input().split(':'))
h2,m2,s2=map(int, input().split(':'))

time1=3600*h1 + 60*m1 + s1
time2=3600*h2 + 60*m2 + s2

if time1>=time2: time2+=3600*24 #하루 뒤가 되는 것이므로
time=time2-time1
print('{:0>2}:{:0>2}:{:0>2}'.format(time//3600,(time%3600)//60,(time%3600)%60))