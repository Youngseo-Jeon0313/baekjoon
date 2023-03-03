import sys
sys.setrecursionlimit(10**6)

def binary(number):
    bin_num=bin(number)[2:]
    for i in range(100):
        if (2**(i-1)-1) < len(bin_num) < 2**i-1 :
            bin_num='0'*((2**i-1)-len(bin_num))+bin_num
    return bin_num
    
    return str(bin(number)[2:])

def check(binary_num, index, length, flag):
    #분할
    if length > 1:
        if binary_num[index+length//2] == '0':
            if not check(binary_num, index+length//2, length//2, False):
                return False
        else:
            if not flag or not check(binary_num, index+length//2, length//2, True):
                return False
        if binary_num[index-length//2] == '0':
            if not check(binary_num, index-length//2, length//2, False):
                return False
        else:
            if not flag or not check(binary_num, index-length//2, length//2, True):
                return False
    #그게 다 아니라면 True를 반환
    return True
    
        
    
def solution(numbers):
    answer = []
    for i in numbers:
        # print(binary(i))
        flag=(binary(i)[len(binary(i))//2]=='1')
        if check(binary(i), len(binary(i))//2,(len(binary(i))+1)//2, flag)==False:
            answer.append(0)
        else : 
            answer.append(1) 
    
    return answer