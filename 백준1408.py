now_h,now_m,now_s=map(int, input().split(':'))
start_h,start_m,start_s=map(int, input().split(':'))

start_time=3600*start_h+60*start_m+start_s
end_time=start_time+3600*24
now_time=3600*now_h+60*now_m+now_s

time=end_time-now_time
if time>3600*24:
    time-=3600*24
print('{:0>2}:{:0>2}:{:0>2}'.format(time//3600,(time%3600)//60,(time%3600)%60))