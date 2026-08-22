n = int(input())

numbers = list(map(int, input().split()))

found = False

for x in numbers:
    if x >= 6:
        if not found:
            max_value = x
            found = True
        elif x > max_value:
            max_value = x

if found:
    print(max_value)
else:
    print("没有符合条件的值")
