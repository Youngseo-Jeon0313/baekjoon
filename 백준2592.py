numbers = [int(input()) for _ in range(10)]
print(sum(numbers)//10)
print(max(numbers, key = numbers.count))