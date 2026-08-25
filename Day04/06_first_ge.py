"""
题目：使用二分查找寻找第一个 >= target 的位置

示例：
nums = [1, 3, 5, 7, 8, 10, 12]
target = 8

输出：
4

思路：
这里不是寻找“target 是否存在”，而是寻找第一个满足
nums[i] >= target 的位置。

当 nums[mid] >= target：
1. mid 可能就是答案，先记录 answer = mid。
2. 但左边可能还有更早的满足条件的位置。
3. 因此继续向左搜索：right = mid - 1。

当 nums[mid] < target：
说明 mid 以及左边都不满足条件，只能向右搜索。

如果不存在满足条件的位置，answer 保持 -1。

重点：
- target 本身不一定存在。
- 这是“找第一个满足条件的位置”的条件二分。
- answer 记录候选答案，right 继续向左缩小。
- target = 0 也可能得到下标 0，例如数组第一个元素为 1。

复杂度：
- 时间：O(log n)
- 空间：O(1)
"""

nums = [1, 3, 5, 7, 8, 10, 12]

target = 8

left = 0

right = len(nums) - 1

answer = -1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] >= target:

        answer = mid

        right = mid - 1

    else:

        left = mid + 1

print(answer)
