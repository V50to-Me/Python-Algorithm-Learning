n = int(input())
numbers = list(map(int, input().split()))

left = [0] * n
right = [0] * n

max_length = 0
current = 0

# 从左向右计算 left[i]
# left[i]：以 i 结尾的连续偶数长度
for i in range(n):
    if numbers[i] % 2 == 0:
        if i == 0:
            left[i] = 1
        else:
            left[i] = left[i - 1] + 1
    else:
        left[i] = 0

# 从右向左计算 right[i]
# right[i]：以 i 开始的连续偶数长度
for i in range(n - 1, -1, -1):
    if numbers[i] % 2 == 0:
        if i == n - 1:
            right[i] = 1
        else:
            right[i] = right[i + 1] + 1
    else:
        right[i] = 0

# 不删除任何元素时的最长连续偶数段
for i in range(n):
    if numbers[i] % 2 == 0:
        current += 1
    else:
        if current > max_length:
            max_length = current
        current = 0

if current > max_length:
    max_length = current

# 尝试删除一个奇数
for i in range(n):
    if numbers[i] % 2 != 0:
        if n == 1:
            candidate = 0
        elif i == 0:
            candidate = right[i + 1]
        elif i == n - 1:
            candidate = left[i - 1]
        else:
            candidate = left[i - 1] + right[i + 1]

        if candidate > max_length:
            max_length = candidate

print(max_length)
