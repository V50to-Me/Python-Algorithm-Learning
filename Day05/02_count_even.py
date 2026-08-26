"""
题目：多次区间偶数计数查询
思路：偶数记为 1，非偶数记为 0，做前缀计数。
prefix[i] 表示 nums[0] 到 nums[i-1] 中偶数的数量。
闭区间 [l, r] = prefix[r + 1] - prefix[l]。
复杂度：O(n + q)，空间 O(n)。
"""

n, q = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0]

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        prefix.append(prefix[i] + 1)
    else:
        prefix.append(prefix[i])

for _ in range(q):
    l, r = map(int, input().split())
    res = prefix[r + 1] - prefix[l]
    print(res)
