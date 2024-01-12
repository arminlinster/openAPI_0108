while True:
    stuff = input("請入小寫英文字[按q會離開]:")
    if(stuff == "q"):
        break
    print(stuff.capitalize())
print("程式結束")