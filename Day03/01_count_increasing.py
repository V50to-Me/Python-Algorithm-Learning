n = int(input())
numbers = list(map(int, input().split()))

count = 0

for i in range(len(numbers) - 1):
    if numbers[i + 1] > numbers[i]:
        count += 1

print(count)
