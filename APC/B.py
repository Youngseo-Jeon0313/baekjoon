from collections import deque

n=int(input())
dict={'@':'a', '[':'c', '!':'i',';':'j','^':'n','0':'o','7':'t','\\\'':'v','\\\\\'':'w'}
for _ in range(n):
    S=input()
    List=[]
    index=0
    
    giveup=0
    while True:
        if index>=len(S): break
        if len(S)-index>=2 and S[index:index+3] in dict.keys(): 
            List.append(dict[S[index:index+3]]); index+=3
            giveup+=1
        elif len(S)-index>=1 and S[index:index+2] in dict.keys():
            List.append(dict[S[index:index+2]])
            index+=2
            giveup+=1
        elif S[index] in dict.keys(): 
            List.append(dict[S[index]])
            index+=1
            giveup+=1
        else: 
            List.append(S[index])
            index+=1

    if giveup>=len(List)/2:print("I don't understand") 
    else:
        for i in List: print(i,end='')
        print()