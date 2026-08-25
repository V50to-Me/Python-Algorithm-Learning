# Day 04 - 排序与二分查找

## 今日目标

从 Day03 的状态维护、边界意识和复杂度分析继续前进，学习：

- `sorted()` 排序
- 线性查找
- 二分查找
- `left / right / mid`
- 闭区间二分
- `O(log n)`
- 找第一个 target
- 找最后一个 target
- 找第一个满足条件的位置
- 排序 + 二分
- 多次查询
- 两次二分统计出现次数
- 二分边界与初始化

---

## 今日学习路线

```text
排序
↓
线性查找
↓
普通二分
↓
二分边界
↓
第一个 target
↓
最后一个 target
↓
第一个 >= target
↓
排序 + 多次二分
↓
两次二分统计出现次数
```

---

## 今日代码

| 文件 | 题目 | 核心知识 |
|---|---|---|
| `01_second_largest.py` | 最大值与第二大的不同值 | 排序、逆序查找 |
| `02_linear_search.py` | 线性查找 target | `for`、`break`、`for...else` |
| `03_binary_search.py` | 判断 target 是否存在 | 基础二分 |
| `04_first_target.py` | 找第一个 target | 左边界 |
| `05_last_target.py` | 找最后一个 target | 右边界 |
| `06_first_ge.py` | 找第一个 `>= target` | 条件二分 |
| `07_sort_and_multi_query.py` | 排序 + 多次边界查询 | 预处理 + 二分 |
| `08_count_frequency_binary_search.py` | 二分统计出现次数 | 两次边界二分 |

---

## 1. 排序与第二大不同值

先使用：

```python
sorted(nums)
```

得到有序数组，再从后往前寻找第一个严格小于最大值的元素。

核心：

```text
最大值
↓
从末尾向前
↓
找到第一个 < 最大值
↓
第二大的不同值
```

排序复杂度为 `O(n log n)`。

---

## 2. 普通二分查找

二分查找要求数组有序。

本 Day 统一使用闭区间：

```text
[left, right]
```

循环条件：

```python
while left <= right:
```

三种情况：

```text
nums[mid] < target
→ left = mid + 1

nums[mid] > target
→ right = mid - 1

nums[mid] == target
→ 找到
```

复杂度：

```text
O(log n)
```

---

## 3. 找第一个 target

找到 target 后不能直接 `break`。

应该：

```text
记录 answer
↓
继续向左
↓
right = mid - 1
```

因为左边可能还有 target。

---

## 4. 找最后一个 target

找到 target 后：

```text
记录 answer
↓
继续向右
↓
left = mid + 1
```

因为右边可能还有 target。

---

## 5. 找第一个满足条件的位置

例如寻找第一个：

```text
nums[i] >= target
```

当：

```python
nums[mid] >= target
```

说明 `mid` 可能是答案：

```text
answer = mid
```

然后继续向左：

```text
right = mid - 1
```

这就是条件二分的基本形式。

---

## 6. 排序 + 多次二分

如果原数组无序：

```text
无序数组
↓
排序一次
↓
多个查询分别二分
```

不要每次查询都重新排序。

总复杂度：

```text
O(n log n + q log n)
```

---

## 7. 两次二分统计出现次数

对于有序数组：

```text
[1, 3, 3, 5, 7, 7, 7, 9]
```

统计 `7`：

```text
第一个 7 的位置 = 4
最后一个 7 的位置 = 6
```

因此：

```text
出现次数 = 6 - 4 + 1 = 3
```

如果第一个位置是 `-1`：

```text
说明不存在
→ 输出 0
```

---

## 今日最重要的原则

### 1. 二分不是死记模板

真正需要理解：

> 当前 `mid` 是否可能是答案？如果可能，答案在哪一侧还可能存在？

---

### 2. 找到答案不一定结束

普通查找：

```text
找到 → break
```

找边界：

```text
找到 → 记录 → 继续搜索
```

---

### 3. 初始化决定程序是否稳定

例如：

```python
answer = -1
```

表示：

```text
目前还没有找到答案
```

如果变量可能没有被赋值，就可能出现：

```text
NameError
```

---

### 4. 循环中的状态不要被重复初始化

错误：

```python
while left <= right:
    answer = -1
```

这样每轮都会清空之前找到的答案。

正确：

```python
answer = -1

while left <= right:
    ...
```

---

### 5. 两次独立二分必须重新初始化搜索区间

```python
left = 0
right = len(nums) - 1
```

第一次二分结束后，第二次二分不能继续使用已经被修改过的 `left/right`。

---

## Day04 易错记录

1. `while left < right` 可能漏掉 `left == right` 的最后一个候选。
2. `answer` 没有初始化可能产生 `NameError`。
3. 将 `answer = -1` 写进循环会导致答案被反复重置。
4. 两次二分没有重新初始化 `left/right`。
5. `-1` 只是“未找到”的标记，不能直接当普通下标参与最终计算。
6. “找第一个 `>= target`”不要求 target 本身存在。
7. 排序 + 二分的总复杂度不能只写成 `O(log n)`，因为排序本身需要 `O(n log n)`。

---

## Day04 复盘

今天从普通二分逐渐过渡到边界二分。

最大的变化：

> 从“我会写二分模板”，开始转向“我能根据题目定义搜索条件和答案边界”。

目前需要继续强化：

- 二分边界
- 初始化
- 不存在答案的情况
- 条件二分
- 复杂度分析
- 从题目中主动判断是否适合二分

---

## 下一步

Day05 不再无目的重复普通二分。

会在保留二分能力的基础上，继续学习百度之星高频基础题型，并开始提高：

- 题型识别速度
- 边界处理速度
- 代码书写速度
- 限时完成能力
