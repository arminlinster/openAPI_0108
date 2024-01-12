try:
    height = float(input('請輸入身高(公分):'))
    print('您的身高:', height, '公分')
    weight = float(input('請輸入體重(公斤):'))
    print('您的體重:', weight, '公斤')
    BMI = weight / (height/100)**2

    print('您的BMI值:', BMI)
    
    if(BMI >= 18.5 and BMI < 24):
        print("體重正常")

    else:
        print("體重須注意")
        
        if(BMI < 18.5):
            print("體重過輕")

        elif(BMI >= 24 and BMI < 27):
            print("體重過重")

        elif(BMI >= 27 and BMI < 30):
            print("輕度肥胖")

        elif(BMI >= 30 and BMI < 35):
            print("中度肥胖")

        else:
            print("重度肥胖")

except:
    print("輸入錯誤! 請輸入數字!!!")