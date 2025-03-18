T=int(input())
for _ in range(T):
    ans_left = 0
    s = input()
    left = 0; right = len(s)-1
    # 다를 때 왼쪽 거를 하나 더
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if ans_left == 1:
                ans_left +=1
                break
            left += 1
            ans_left += 1
    ans_right = 0
    left = 0; right = len(s)-1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if ans_right == 1:
                ans_right +=1
                break
            right -= 1
            ans_right += 1
    print(min(ans_left, ans_right))