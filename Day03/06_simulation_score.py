score = 0

n = int(input())
s = input()

for c in s:
    if c == 'A':
        score += 3
    elif c == 'B':
        score -= 2
    elif c == 'C':
        score *= 2

print(score)
