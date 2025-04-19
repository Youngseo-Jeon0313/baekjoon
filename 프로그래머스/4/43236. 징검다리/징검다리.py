def solution(distance, rocks, n):
    answer = 0
    
    rocks.append(distance)
    rocks = sorted(rocks)
    
    left, right = 0, distance  
    
    while left <= right:
        
        mid = (left + right) // 2  
        min_distance = float('inf')  
        current = 0  
        remove_cnt = 0  
        
        for rock in rocks:
            diff = rock - current  
            if diff < mid:  
                remove_cnt += 1
            else:  
                current = rock  
        
        if remove_cnt > n:  
            right = mid - 1
        else:  
            answer = mid
            left = mid + 1

    return answer