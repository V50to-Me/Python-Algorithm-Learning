"""
【题目】学生排名（三关键字排序）
n 名学生，每人有：名字、分数、年龄。
排名规则（依次比较）：
1. 分数高的在前；
2. 分数相同，年龄小的在前；
3. 分数年龄都相同，名字字典序小的在前。
输出排序后名单，每行"名字 分数 年龄"。

【输入】
第一行：n
接下来 n 行：名字 分数 年龄

【示例】
输入：               输出：
5                    Carol 92 11
Tom 85 12            Jerry 92 11
Jerry 92 11          Bob 92 13
Alice 85 10          Alice 85 10
Bob 92 13            Tom 85 12
Carol 92 11

【思路】
和多关键字两条件版完全同构，只是 key 的元组变长：
key 返回 (-分数, 年龄, 名字)
- 第 0 位：分数取负 → 降序
- 第 1 位：年龄保持原样 → 升序（小的在前）
- 第 2 位：名字保持原样 → 字典序升序
元组比较会自动按顺序依次比较，打平才看下一位。

【核心知识点】
- 多关键字排序：条件有几个，key 元组就有几位
- 每一位的正负（取负 = 该位降序）按题意逐位决定

【复杂度】
O(n log n)

【踩坑记录】
- 年龄也是数字，能不能取负要看题意：这题要"年龄小的在前"即升序，
  所以保持原样，不取负——不是所有数字都取负，逐位按题意判断
- 输出时用序列解包 for name, score, age in result，
  比下标 result[i][1] 更不容易取错位置
"""

n = int(input())
students = []
for _ in range(n):
    name, score, age = input().split()
    students.append((int(score), int(age), name))

result = sorted(students, key=lambda t: (-t[0], t[1], t[2]))

for name, score, age in result:
    print(name, score, age)
