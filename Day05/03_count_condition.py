"""
题目：多次区间条件计数查询
题目：统计每个 [l, r] 中 >= 5 的数字数量。
思路：满足条件记为 1，否则记为 0，再做前缀计数。
prefix[i] 表示 nums[0] 到 nums[i-1] 中 >= 5 的数量。
复杂度：O(n + q)，空间 O(n)。
"""

n, q = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0]

for i in range(len(nums)):
    if nums[i] >= 5:
        prefix.append(prefix[i] + 1)
    else:
        prefix.append(prefix[i])

for _ in range(q):
    l, r = map(int, input().split())
    res = prefix[r + 1] - prefix[l]
    print(res)
