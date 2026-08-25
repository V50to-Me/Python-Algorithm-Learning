"""
题目：在线性数组中查找 target 是否存在

示例：
nums = [1, 3, 5, 7, 9, 12, 15, 20]
target = 12

输出：
找到

思路：
从数组左到右依次检查每个元素。
如果当前元素等于 target，就输出“找到”并使用 break 提前结束。
如果整个循环都没有 break，则执行 for...else 中的“不存在”。

重点：
- 线性查找不要求数组有序。
- break 可以提前终止循环。
- Python 的 for...else 中，else 会在循环正常结束、没有执行 break 时执行。

复杂度：
- 时间：O(n)
- 空间：O(1)
"""

nums = [1, 3, 5, 7, 9, 12, 15, 20]

target = 12

for i in nums:

    if i == target:

        print("找到")

        break

else:

    print("不存在")
