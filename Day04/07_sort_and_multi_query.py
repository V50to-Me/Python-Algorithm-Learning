"""
题目：无序数组 + 多次查询，寻找第一个 >= x 的位置

输入：
第一行：n q
第二行：n 个整数（原数组不保证有序）
接下来 q 行：每行一个查询 x

要求：
对每个 x，输出排序后的数组中第一个 >= x 的下标。
不存在则输出 -1。

示例输入：
7 5
7 2 15 3 9 1 12
3
8
10
16
0

输出：
2
4
5
-1
0

思路：
1. 原数组无序，不能直接二分。
2. 只排序一次。
3. 每个查询都重新初始化 left/right。
4. 使用“第一个 >= x”的边界二分。

重点：
- 不要每次查询都重新排序。
- 多次查询使用同一个排序后的数组。
- 每次查询都是独立的二分，因此 left/right 必须重新初始化。
- 排序一次 + q 次二分。

复杂度：
- 排序：O(n log n)
- q 次查询：O(q log n)
- 总复杂度：O(n log n + q log n)
- 本实现额外保存 q 个查询，空间为 O(n + q)（排序后的 nums 本身为 O(n)）。
"""

n, q = map(int, input().split())

nums = sorted(list(map(int, input().split())))

target = []

for i in range(q):

    target.append(int(input()))

for x in target:

    left = 0

    right = len(nums) - 1

    answer = -1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] >= x:

            right = mid - 1

            answer = mid

        else:

            left = mid + 1

    print(answer)
