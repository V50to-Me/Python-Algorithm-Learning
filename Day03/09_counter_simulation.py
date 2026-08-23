value = 0

n = int(input())
s = input()

for c in s:
    if c == '+':
        value += 1
    elif c == '-':
        value -= 1

    if value < 0:
        break

print(value)
