def countWaysToColorHouses(n):
    ans = 6*3**(n//2-1) 
    return ans%(10**9+7)