#1~100加總
value = 1
n = 0
while value <= 100:
    n += value
    value += 1
print("第一種 while")
print(n)
value = 1
total = 0
while True:
    total += value
    value += 1
    if value > 100:
        break
print("第二種 while")
print(total)
