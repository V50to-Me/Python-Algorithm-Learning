"""
题目：
给定一个整数数组，最多删除一个奇数，
求删除后最长连续偶数段的长度。

连续偶数：
数组位置连续，并且每个元素都是偶数。

示例：
输入：
6
2 4 6 3 8 10

输出：
5

--------------------------------------------------

解题思路：

1. 先计算原数组中最长连续偶数段。
2. 使用 left[i] 记录以 i 结尾的连续偶数长度。
3. 使用 right[i] 记录以 i 开始的连续偶数长度。
4. 枚举每一个奇数作为删除位置。
5. 如果删除中间的奇数：
   candidate = left[i - 1] + right[i + 1]
6. 更新最大答案。

--------------------------------------------------

核心知识点：

- 状态维护
- 左右预处理
- 边界处理
- 候选答案
- O(n) 时间复杂度
- O(n) 空间复杂度

--------------------------------------------------

踩坑记录：

1. 不能把 max_length 初始化成任意数字。
2. 删除位置位于开头或结尾时，需要单独处理。
3. 不能只保存最后一次 candidate，
   每个 candidate 都应该立即参与 max_length 更新。
"""

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
