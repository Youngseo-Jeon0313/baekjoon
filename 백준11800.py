p1 = {1 : "Yakk", 2 : "Doh", 3 : "Seh",
      4 : "Ghar", 5 : "Bang", 6 : "Sheesh"}
p2 = {1 : "Habb Yakk", 2 : "Dobara", 3 : "Dousa",
      4 : "Dorgy", 5 : "Dabash", 6 : "Dosh"}

t=int(input())
for i in range(t):
    a, b = map(int, input().split())
    #예외
    if (a==5 and b==6) or(a==6 and b==5) : print('Case {}: Sheesh Beesh'.format(i+1))
    #같으면 p2대로 가기
    elif a==b: print('Case {}: {}'.format(i+1, p2[a]))
    #다르면 p1이랑 p1 이렇게
    else: print('Case {}: {} {}'.format(i+1, p1[max(a,b)], p1[min(a,b)]))