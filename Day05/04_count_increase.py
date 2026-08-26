"""
题目：多次区间相邻上升次数查询
定义：如果 nums[i] > nums[i - 1]，则发生一次上升。
prefix[i] 表示 nums[0] 到 nums[i] 之间发生的上升次数。
因此查询闭区间 [l, r] 时：
    prefix[r] - prefix[l]

注意：
这里 prefix 的定义和普通前缀和不同，所以不能机械套用
prefix[r + 1] - prefix[l]。
复杂度：O(n + q)，空间 O(n)。
"""

n, q = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0]

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        prefix.append(prefix[i - 1] + 1)
    else:
        prefix.append(prefix[i - 1])

for _ in range(q):
    l, r = map(int, input().split())
    res = prefix[r] - prefix[l]
    print(res)
