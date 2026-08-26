"""
题目：多次区间求和查询
思路：构造 prefix，prefix[i] 表示 nums[0] 到 nums[i-1] 的和。
闭区间 [l, r] 的和 = prefix[r + 1] - prefix[l]。
复杂度：预处理 O(n)，单次查询 O(1)，总计 O(n + q)，空间 O(n)。
"""

n, q = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0]

for i in range(len(nums)):
    prefix.append(prefix[i] + nums[i])

for _ in range(q):
    l, r = map(int, input().split())
    res = prefix[r + 1] - prefix[l]
    print(res)
