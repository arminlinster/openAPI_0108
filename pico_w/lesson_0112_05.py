def BMI(height_box,weight_box):
    bmi = weight_box / (height_box / 100) ** 2
    return bmi
print(BMI(170,70))