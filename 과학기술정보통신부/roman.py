dct1={
    'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
}
dct2={
    'IV':4, 'IX':9, 'XL':40,
    'XC':90, 'CD': 400, 'CM':900
}

a=input()

idx=0; num=0;
while idx<len(a):
    cur = a[idx]
    if cur in 'IXC' and idx != len(a)-1:
        next = a[idx+1]
        if cur+next in dct2:
            num += dct2[cur+next]
            idx+=2
            continue
    num +=dct1[cur]
    idx+=1

print(num)