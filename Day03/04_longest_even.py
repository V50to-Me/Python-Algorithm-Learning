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

'''
遇到奇数：
先保存 current
再 current = 0

遍历结束：
还要再检查一次 current
'''
