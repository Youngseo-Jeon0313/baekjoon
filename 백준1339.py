#0 1 2 3 4 5 6 7 8 9 
N=int(input()) #1이상 10이하
L=list()
Sort=[]
alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
for _ in range(N): L.append(input())
for i in L:
    for j in range(len(i)):
        alphabet_dict[i[j]]+=1*10**(len(i)-j)
alphabet_dict=sorted(alphabet_dict.items(),key=(lambda x:x[1]), reverse=True)
sum=0
i=9
for j in alphabet_dict:
    if j[1]==0: continue
    sum+=j[1]*i
    i-=1
print(sum//10)