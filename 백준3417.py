while True:
    key=input()
    if key=='0':
        break
    solve=list(input())
    for i in range(len(solve)):
        #0을 기준으로 만들고 둘을 더한 다음에 
        solve[i]=(ord(solve[i])-65+ord(key[i%len(key)])-64)%26+65
        solve[i]=chr(solve[i])
    print(''.join(solve))