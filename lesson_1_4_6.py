weight = int(input("請輸入您的start number:"))
Height = int(input("請輸入您的end number:"))
n=0
for i in range(weight, Height+1):
    n += i
print(n)