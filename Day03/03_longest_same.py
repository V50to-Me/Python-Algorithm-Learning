n = int(input())
numbers = list(map(int, input().split()))

current = 1
max_length = 1

for i in range(len(numbers) - 1):
    if numbers[i + 1] == numbers[i]:
        current += 1
    else:
        current = 1

    if current > max_length:
        max_length = current

print(max_length)
