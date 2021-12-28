#강력한 표준 자료형들을 잘 다뤄보자.
"""
a=1000
print(a)

a=-7
print(a)

a=0
print(a)

print(1e9)
print(round(0.3+0.6,2))

list 자료형
a=[1,3,5,2,4]

print(a)

array=[i for i in range(10)]
print(array)

array = [i for i in range(20) if i%2 ==1]
print(array)
-> array.append(i) 로 구현하는 것보다 빠름


2차원 리스트 만드는 방법
array = [[0]*m for i in range(n)]

m=2
n=3
array = [[0]*m] *n
이건 살짝 잘못됨 한 '칸'을 취급하고 싶은 경우인데
한 '열'을 취급하게 될 수 있음

print(array)

append
sort 오름차순 sort(reverse=True) 내림차순
reverse
insert 삽입
count
remove / 집합 자료형을 통해 특정 값을 가지는 원소를 모두 제거 가능 remove_set={3,5}

문자열은 indexing은 가능하다 값을 변경할 수 없다.

튜플은 ()소괄호 이용함, 값 변경 불가능, indexing 가능
a=(1,3,4,2,5,6,7)
print(a) 
서로 다른 성질의 데이터를 묶어서 관리해야 할 때

dictionary 자료형 , key-value가 있는 게 포인트
data=dict()
data['사과'] ='Apple'
data['바나나'] ='Banana'
data={
    '사과'='apple',
    '바나나'='banana'
}
print(data)

print(data.keys())
keys()  values() 함수 사용 가능


집합
set()
data={1,1,2,3,3,4,5} 중괄호

합집함 | 교집합 & 차집합 -


list(map(int, input().split()))
많이 쓰임. 공백을 기준으로 구분하여 입력받고 list형으로 전환
그리고 input은 일단 str으로 받기 때문에 그걸 int로 바꿔준다.


f string 예제
answer = 7
print(f"정답은 {answer}입니다")


"""




