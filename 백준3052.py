#python 중복요소 counting하기
# try, except 문 사용하기

count = {}
list_num=[]

for i in range(10):
    b=int(input())
    list_num.append(b%42)


for i in list_num:
    try: count[i] += 1
    except: count[i] = 1

# 여기서 count라는 set을 만들고(set은 집합) 그 후에 
# 시도를 해보는 거지
# 원래 있었다면 count[i]를 하나 더하기
# 없다면 count[i]를 1로 하나 만들기!

print(len(count))
