midterm = int(input())
finalterm = int(input())
average = (midterm+finalterm)/2

flag=True
if average>=90: print("훌륭하네요"); flag=False
if average>=60 and flag: print("잘했어요"); flag=False
else:
    if flag:
        print("내년에 다시 봐요")