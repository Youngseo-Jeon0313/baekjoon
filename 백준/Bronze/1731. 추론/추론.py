N=int(input())
List=[]
for i in range(N):
    List.append(int(input()))
if List[2]/List[1] == List[1]/List[0]:
    print(List[2]//List[1]*List[-1])
else: print(int(List[2]-List[1]+List[-1]))