total = 0
while True:
    number1 = int(input("請輸入數字[按負整數會離開]:"))
    if number1 < 0:
        break
    if number1 %2 == 1:
        continue
    else:
        total += number1
    print(total)
print("程式結束")