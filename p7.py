# Q7.Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"
 
def bmi(height,weight):
    bmi=weight/(height**2)
    return bmi
height=1.79832
weight=70
bmi = bmi(height, weight)
print("The BMI is", format(bmi), "so ", end='')
if (bmi<18.5):
    print("underweight")
elif (bmi >=18.5 and 25.9):
    print ("Normal")
elif (bmi>=25.9 and bmi<30):
    print ("overweight")
elif (bmi>=30):
    print("suffering from obesity")              

