p1 = {1 : "Yakk", 2 : "Doh", 3 : "Seh",
      4 : "Ghar", 5 : "Bang", 6 : "Sheesh"}
p2 = {1 : "Habb Yakk", 2 : "Dobara", 3 : "Dousa",
      4 : "Dorgy", 5 : "Dabash", 6 : "Dosh"}

t=int(input())
for i in range(t):
    a, b = map(int, input().split())
    if (a==5 and b==6) or (a==6 and b==5) : print('Case {}: Sheesh Beesh'.format(i+1))
    elif a==b: print('Case {}: {}'.format(i+1, p2[a]))
    else: print('Case {}: {} {}'.format(i+1, p1[b], p1[a]))