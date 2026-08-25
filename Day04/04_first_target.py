"""
题目：使用二分查找寻找 target 第一次出现的位置

示例：
nums = [1, 2, 2, 2, 3, 5, 5, 8]
target = 2

输出：
1

思路：
普通二分找到 target 后不能直接 break，因为当前 target
可能不是第一次出现的位置。

找到 target：
1. 记录当前下标 answer = mid。
2. 继续向左搜索。
3. 因此执行 right = mid - 1。

如果 target 不存在，answer 保持 -1。

重点：
- “找到一个”与“找到第一个”不同。
- answer 必须在 while 循环外初始化。
- 找到 target 后继续向左，而不是 break。
- -1 表示没有找到。

复杂度：
- 时间：O(log n)
- 空间：O(1)
"""

nums = [1, 2, 2, 2, 3, 5, 5, 8]

target = 2

left = 0

right = len(nums) - 1

answer = -1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:

        right = mid - 1

        answer = mid

    elif nums[mid] > target:

        right = mid - 1

    elif nums[mid] < target:

        left = mid + 1

print(answer)
