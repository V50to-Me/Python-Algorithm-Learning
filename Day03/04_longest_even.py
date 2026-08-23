n = int(input())
numbers = list(map(int, input().split()))

current = 0
max_length = 0

for x in numbers:
    if x % 2 == 0:
        current += 1
    else:
        if current > max_length:
            max_length = current
        current = 0

if current > max_length:
    max_length = current

print(max_length)
