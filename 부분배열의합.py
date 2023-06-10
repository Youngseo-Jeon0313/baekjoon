def dynamic_partial_sum(arr):
    cache = [0] * len(arr)
    cache[0] = arr[0]
    for i in range(0, len(arr)):
        cache[i] = max(0, cache[i-1]) + arr[i]
    return max(cache)

print(dynamic_partial_sum([-2,-3,4,-1,-2,1,5,-3]))