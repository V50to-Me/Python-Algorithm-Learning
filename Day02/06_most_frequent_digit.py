s = input()

counts = {}

for c in s:
    if c.isdigit():
        counts[c] = counts.get(c, 0) + 1

values = list(counts.values())

max_values = values[0]

for val in values:
    if val > max_values:
        max_values = val

keys = [k for k, v in counts.items() if v == max_values]

num = keys[0]

for n in keys[1:]:
    if n < num:
        num = n

print(num)
