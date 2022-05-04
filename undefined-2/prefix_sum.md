# prefix\_sum

\#정의

부분합(partial sum)과의 차이??

\#팁

1차원과 2차원이 살짝 다르다. 2차원의 경우 점 세개만 기억하자!

\#조건

* psum을 만들 시 0행과 0열 모두 0으로  초기화해서 하나 더해준다.

\#코드

```
r,c,q=map(int,input().split())
arr =[[*map(int,input().split())] for _ in range(r)]
psum=[[0]*(c+1) for _ in range(r+1)]
for i in range(1, r+1):
    for j in range(1,c+1):
        psum[i][j]=psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]+arr[i-1][j-1]

for i in range(q):
    r1,c1,r2,c2=map(int,input().split())
    print((psum[r2][c2]-psum[r2][c1-1]-psum[r1-1][c2]+psum[r1-1][c1-1])//((r2-r1+1)*(c2-c1+1)))
```

{% tabs %}
{% tab title="백준11441" %}

{% endtab %}

{% tab title="백준1806" %}

{% endtab %}

{% tab title="백준1644" %}

{% endtab %}

{% tab title="백준2015" %}

{% endtab %}
{% endtabs %}
