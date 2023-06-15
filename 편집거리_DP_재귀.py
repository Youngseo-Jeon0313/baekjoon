def edit_distance_recursive(str1, str2):
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    elif str1[-1] == str2[-1]:
        return edit_distance_recursive(str1[:-1], str2[:-1])
    else:
        insertion = edit_distance_recursive(str1, str2[:-1])
        deletion = edit_distance_recursive(str1[:-1], str2)
        substitution = edit_distance_recursive(str1[:-1], str2[:-1])
        return min(insertion, deletion, substitution) + 1

# 테스트
string1 = "kitten"
string2 = "sitting"
distance = edit_distance_recursive(string1, string2)
print(f"편집 거리: {distance}")
