n = int(input())

numbers = list(map(int, input().split()))

max_sum = numbers[0] + numbers[1]

for i in range(n):
    for j in range(i + 1, n):
        current_sum = numbers[i] + numbers[j]

        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)
