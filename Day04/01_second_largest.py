"""
题目：在数组中寻找最大值和第二大的不同值

示例：
nums = [7, 2, 9, 1, 5, 3]
输出：
[1, 2, 3, 5, 7, 9]
9
7

思路：
1. 使用 sorted() 将数组升序排序。
2. 最后一个元素就是最大值。
3. 从数组末尾向前寻找第一个严格小于最大值的元素。
4. 这个元素就是第二大的不同值。

重点：
- 第二大要求“不同值”，所以使用 nums_sort[i] < max_value。
- 从后往前找可以直接定位第二大的不同值。
- 如果所有元素都相同，则不存在第二大的不同值，需要额外处理。

复杂度：
- 排序：O(n log n)
- 从后向前查找：O(n)
- 总复杂度：O(n log n)
"""

nums = [7, 2, 9, 1, 5, 3]

nums_sort = sorted(nums)

max_value = nums_sort[len(nums) - 1]

sec_value = nums_sort[0]

for i in range(len(nums) - 1, -1, -1):

    if nums_sort[i] < max_value:

        sec_value = nums_sort[i]

        break

print(nums_sort)
print(max_value)
print(sec_value)
