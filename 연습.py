import sys
import math

def 카드섞기(n, k, arr):

    arr = arr[n-(2 ** k):] + arr[:n-(2 ** k)]; #step1
    # print('step1 ', k, arr);
    last_move = (2**k) -1;
    for i in range(2,k+2):
        ea = (2 ** (k-i+1));
        arr = arr[last_move -ea +1 : last_move +1] + arr[:last_move - ea +1] + arr[last_move +1 :];
        last_move = ea -1;
        # print('step',i, ' ', k, arr);
    return arr;

def solution(n, answer):

    in_arr = list(range(1,n+1));
    max_k =  math.ceil(math.log2(n));
    for i in range(1, max_k):
        result = 카드섞기(n, i,in_arr);
        # print(i, result);
        for j in range(1, max_k):
            result2 = 카드섞기(n, j, result);
            print(*result2)
            if answer == result2:
                print(i, j);
                return;

n = int(sys.stdin.readline());
myList = list(map(int,sys.stdin.readline().split()));
solution(n, myList);