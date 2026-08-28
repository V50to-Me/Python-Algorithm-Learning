"""
题目：
给定一个升序数组 nums 和 target，判断是否存在两个不同元素之和等于 target。

示例：
nums = [1, 2, 3, 4, 6, 8, 10]
target = 13

思路：
使用相向双指针。
如果 nums[L] + nums[R] > target，R 左移；
如果小于 target，L 右移；
相等则找到答案。

复杂度：
时间 O(n)
空间 O(1)
"""

nums = [1, 2, 3, 4, 6, 8, 10]
target = 13

L = 0
R = len(nums) - 1

while L <= R:
    if nums[L] + nums[R] > target:
        R -= 1
    elif nums[L] + nums[R] < target:
        L += 1
    else:
        print("存在")
        break
else:
    print("不存在")
