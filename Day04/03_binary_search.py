"""
题目：使用二分查找判断 target 是否存在

示例：
nums = [1, 3, 5, 7, 9, 12, 15, 20]
target = 15

输出：
存在

思路：
1. 二分查找要求数组有序。
2. 使用闭区间 [left, right] 表示当前搜索范围。
3. 每次取中点 mid。
4. nums[mid] < target：答案只可能在右侧。
5. nums[mid] > target：答案只可能在左侧。
6. 相等时找到 target。

重点：
- 使用 while left <= right。
- 使用 mid + 1 和 mid - 1 排除已经检查过的 mid。
- left/right 都是下标。
- 二分每次将搜索空间缩小约一半。

复杂度：
- 时间：O(log n)
- 空间：O(1)
"""

nums = [1, 3, 5, 7, 9, 12, 15, 20]

target = 15

left = 0

right = len(nums) - 1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] < target:

        left = mid + 1

    elif nums[mid] > target:

        right = mid - 1

    else:

        print("存在")

        break

else:

    print("不存在")
