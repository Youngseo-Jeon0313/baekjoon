def kmp(all_string, pattern):
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1,len(pattern)):
        while i>0 and pattern[i]!=pattern[j]:
            i = table[i-1]
        if pattern[i]==pattern[j]:
            i+=1
            table[j]=i

    result =[]
    i=0
    for j in range(len(all_string)):
        while i>0 and pattern[i] != all_string[j]:
            i = table[i-1]
        if pattern[i]==all_string[j]:
            i+=1