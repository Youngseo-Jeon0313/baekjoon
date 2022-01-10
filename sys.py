#sys 모듈을 이용해서 빠르게 입력받기

#숫자
input = __import__('sys').stdin.readline
x=int(input())
a, b = map(int, input().split())

#문자열
input=__import__('sys').stdin.readline
x = input().strip()
a, b= input().strip().split()

