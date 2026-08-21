students = [
    {"name": "张三", "age": 18, "score": 85},
    {"name": "李四", "age": 19, "score": 92},
    {"name": "王五", "age": 18, "score": 76}
]

name = input("请输入要查询的学生姓名：")

found = False

for student in students:

    if name == student["name"]:
        found = True

        print("姓名：", student["name"])
        print("年龄：", student["age"])
        print("分数：", student["score"])

        break

if found == False:
    print("没有找到该学生")
