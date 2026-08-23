n, target = map(int, input().split())

numbers = list(map(int, input().split()))

seen = set()

find = False

for x in numbers:
    if target - x in seen:
        find = True
        break

    seen.add(x)

if find:
    print("Yes")
else:
    print("No")
