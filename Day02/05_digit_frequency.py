s = input()

counts = {}

for c in s:
    if c.isdigit():
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1

for key, value in counts.items():
    print(f"{key}:{value}")
