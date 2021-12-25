"""
for k in range(5):
    print (2*k+1)
for i in range(10, 100):
    sum=0
    for j in range (9, i):
        if (j+(j//10)+(j%10))==i :
            sum+=1
        else :
            continue
    if sum==0 :
      print (i)

""" 
#이게 왜 이렇게 하면 안되냐면 1부터 100까지는 이런 식으로 10으로 나눠서 하면 되지만
#100부터 1000까지는 또 100으로 나누는 그런 식으로 가야 함. 
#그래서 애초에 그냥 이 숫자 자체를 string으로 만들어버린 후 다시 숫자로 바꾸는 게 나은 거임.