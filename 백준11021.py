test_case = int(input())


for i in range(test_case): 
    input_data= input().split(' ') #input을 여기서 받는 형태니까 for문이 계속 돌 때마다 input 요구
    A=int(input_data[0])
    B=int(input_data[1])
    print('Case #',i+1,': ',A+B,sep='')
