
try:
    while True:
        A, B= map(int, input().split()) #만약 input해서 받은 내용이 int라면 map질을 해라
        print(A + B)
except: #try에 대한 에러가 발생한 경우 
    exit()

