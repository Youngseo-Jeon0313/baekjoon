a,b,c,d,r=map(int,input().split())
#겹치는 부분을 뺀다.
overlap_width = min(a+r, c+r)-max(a,c)
overlap_height = min(b+r, d+r)-max(b,d)


if overlap_width <=0 or overlap_height<=0: overlap_area = 0
else: overlap_area = overlap_height*overlap_width

result = r*r*2 - overlap_area
print(result)