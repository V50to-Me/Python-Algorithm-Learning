temperature = 20

n = int(input())
s = input()

for c in s:
    if c == 'A':
        temperature += 5
    elif c == 'B':
        temperature -= 3
    elif c == 'C':
        temperature *= 2

    if temperature > 100:
        break

print(temperature)
