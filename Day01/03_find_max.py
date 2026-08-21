numbers = [3, 8, 2, 10, 5, 7]

max_value = numbers[0]

for i in range(1, len(numbers)):

    if max_value < numbers[i]:
        max_value = numbers[i]

print(max_value)
