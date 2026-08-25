"""
题目：使用两次二分查找统计 x 在有序数组中的出现次数

输入：
第一行：n q
第二行：n 个已经有序的整数
接下来 q 行：每行一个查询 x

对于每个 x，输出 x 出现的次数。

示例输入：
10 5
1 3 3 5 7 7 7 9 10 12
7
3
1
6
12

输出：
3
2
1
0
1

思路：
1. 第一次二分寻找 x 最后一次出现的位置 right_value。
   找到 x 后继续向右：left = mid + 1。
2. 第二次二分寻找 x 第一次出现的位置 left_value。
   找到 x 后继续向左：right = mid - 1。
3. 如果 left_value == -1，说明 x 不存在，答案为 0。
4. 否则：
   count = right_value - left_value + 1

重点：
- 两次二分是两个独立的搜索过程，第二次必须重新设置
  left = 0 和 right = len(nums) - 1。
- right_value 和 left_value 必须在 while 循环外初始化为 -1，
  否则每一轮循环都会把之前找到的答案重置。
- -1 是“没有找到”的状态标记，不能直接参与次数计算。
- 出现次数 = 最后位置 - 第一个位置 + 1。

复杂度：
- 每次查询进行两次 O(log n) 二分，仍然是 O(log n)。
- q 次查询：O(q log n)。
- 额外空间：O(1)（不保存所有查询）。
"""

n, q = map(int, input().split())

nums = list(map(int, input().split()))

for _ in range(q):

    x = int(input())

    left = 0

    right = len(nums) - 1

    right_value = -1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] < x:

            left = mid + 1

        elif nums[mid] > x:

            right = mid - 1

        else:

            left = mid + 1

            right_value = mid

    left = 0

    right = len(nums) - 1

    left_value = -1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] < x:

            left = mid + 1

        elif nums[mid] > x:

            right = mid - 1

        else:

            right = mid - 1

            left_value = mid

    if left_value == -1:

        print(0)

    else:

        count = right_value - left_value + 1

        print(count)
