#學生總分為300
#檢查必需300分以內,0分以上
#有些學生可以加分5%
#如果加分超過300,就以300分為準
try:
    scores = int(input("請輸入學生分數(最高300):"))
    if scores <= 300 and scores >= 0:
        is_add = input("學生是否符合加分條件?(y,n):")
        #巢狀判斷
        if(is_add=="y"):
            scores *= 1.05
            if scores > 300:
                scores = 300
        print(round(scores))
    else:
        print("輸入錯誤!")
except:
    print("請輸入數字!")