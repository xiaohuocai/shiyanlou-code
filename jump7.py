a = 0
for i in range(101):
    b = i
    if b % 7 == 0 or b % 10 == 7 or b // 10 == 7:
        continue
    print(b)
