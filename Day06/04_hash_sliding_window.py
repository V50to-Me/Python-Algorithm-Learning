"""
题目：
找最长连续子数组，使其中不同元素的数量 <= 2。

示例：
nums = [1, 2, 1, 2, 3, 1, 2]

答案：
4
对应窗口：[1, 2, 1, 2]

思路：
使用 freq 哈希表维护当前窗口中每个元素的出现次数。
R 加入元素时频次 +1。
当不同元素数量超过 2 时，移动 L：
频次 -1；如果频次变成 0，则删除该 key。
窗口恢复合法后更新最大长度。

复杂度：
时间 O(n)
空间 O(k)，k 为窗口中不同元素数量。
"""

nums = [1, 2, 1, 2, 3, 1, 2]

L = 0
max_length = 0
freq = {}

for R in range(len(nums)):
    freq[nums[R]] = freq.get(nums[R], 0) + 1

    while len(freq) > 2:
        freq[nums[L]] -= 1

        if freq[nums[L]] == 0:
            del freq[nums[L]]

        L += 1

    length = R - L + 1

    if length > max_length:
        max_length = length

print(max_length)
