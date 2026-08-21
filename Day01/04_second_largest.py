numbers = [3, 8, 2, 10, 5, 7, 10, 4]

fst = numbers[0]
found_sec = False

for i in range(1, len(numbers)):
    if fst != numbers[i]:
        sec = numbers[i]
        sec_index = i
        found_sec = True
        break

if found_sec == False:
    print("不存在第二大的不同数字")

else:
    if fst < sec:
        fst, sec = sec, fst

    for i in range(sec_index + 1, len(numbers)):

        if fst < numbers[i]:
            sec = fst
            fst = numbers[i]

        elif fst > numbers[i] and sec < numbers[i]:
            sec = numbers[i]

    print(sec)
