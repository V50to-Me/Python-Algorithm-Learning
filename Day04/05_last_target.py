"""
题目：使用二分查找寻找 target 最后一次出现的位置

示例：
nums = [1, 2, 2, 2, 3, 5, 5, 8]
target = 2

输出：
3

思路：
普通二分找到 target 后不能直接 break，因为当前 target
可能不是最后一次出现的位置。

找到 target：
1. 记录当前下标 answer = mid。
2. 继续向右搜索。
3. 因此执行 left = mid + 1。

如果 target 不存在，answer 保持 -1。

重点：
- 找最后一个 target 时继续向右。
- answer 必须在循环外初始化。
- left = mid + 1 可以排除已经检查过的 mid。
- 与“找第一个 target”的区别主要在于找到 target 后移动哪一侧边界。

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

    if nums[mid] < target:

        left = mid + 1

    elif nums[mid] > target:

        right = mid - 1

    else:

        left = mid + 1

        answer = mid

print(answer)
