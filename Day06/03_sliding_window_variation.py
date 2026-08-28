"""
题目：
找出和 <= 6 的最长连续子数组长度。

示例：
nums = [2, 1, 3, 2, 4, 1]

思路：
使用同向双指针维护一个合法窗口。
R 负责扩张，L 在 sum > 6 时不断收缩。

复杂度：
时间 O(n)
空间 O(1)
"""

nums = [2, 1, 3, 2, 4, 1]

L = 0
max_length = 0
sum = 0

for R in range(len(nums)):
    sum += nums[R]

    while sum > 6:
        sum -= nums[L]
        L += 1

    length = R - L + 1

    if length > max_length:
        max_length = length

print(max_length)
