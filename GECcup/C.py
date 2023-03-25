school_list=[
 "northlondo",
 "branksomeh",
 "koreainter",
 "stjohnsbur"
 ]
SCHOOL=[
    "NLCS",
    "BHA",
    "KIS",
    "SJA"
]

n=input()
school_decode=[]
for z in range(26):
    for index in range(4):
        i=school_list[index]
        temp=[]
        for j in i:
            temp.append(chr((ord(j)+z-97)%26+97))
        # print(str(temp))
        if temp==list(n): print(SCHOOL[index])


# print(school_decode)

# compare=[]

# for x in n:
#     compare.append((ord(x)-z-97)-97%26)

# compare=sorted(compare)

# def prefix_sum(arr):
#     temp=[0]
#     for i in range(1,10):
#         temp.append(arr[i]-arr[i-1])
#     return temp

# # print(prefix_sum(compare))

# # for i in school_decode:
# #     print(prefix_sum(i))
# if prefix_sum(compare)==prefix_sum(school_decode[0]): print("NLCS")
# elif prefix_sum(compare)==prefix_sum(school_decode[1]): print("BHA")
# elif prefix_sum(compare)==prefix_sum(school_decode[2]): print("KIS")
# elif prefix_sum(compare)==prefix_sum(school_decode[3]): print("SJA")