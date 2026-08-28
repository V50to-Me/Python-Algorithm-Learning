"""
题目：
找出和 <= 7 的最长连续子数组长度。

示例：
nums = [2, 1, 5, 1, 3, 2]

思路：
R 不断向右扩张窗口；
如果窗口和超过 7，就移动 L 收缩；
窗口恢复合法后更新最大长度。

复杂度：
时间 O(n)
空间 O(1)
"""

nums = [2, 1, 5, 1, 3, 2]

L = 0
max_length = 0
sum = 0

for R in range(len(nums)):
    sum += nums[R]

    while sum > 7:
        sum -= nums[L]
        L += 1

    length = R - L + 1

    if length > max_length:
        max_length = length

print(max_length)
