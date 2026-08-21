scores = []

for i in range(1, 6):
    x = int(input("请输入第{}个学生的成绩：".format(i)))
    scores.append(x)

print("最高分：", max(scores))
print("最低分：", min(scores))
print("平均分：", sum(scores) / len(scores))
print("及格人数：", len([x for x in scores if x >= 60]))
print("优秀人数：", len([x for x in scores if x >= 90]))
