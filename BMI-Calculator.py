# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print("Your BMI is ", bmi, ", you are underweight.")
elif 18.5 < bmi < 25:
    print("Your BMI is ", bmi, ", you have normal weight.")
elif 25 < bmi < 30:
    print("Your BMI is ", bmi, ", you are slightly over weight.")
elif 30 < bmi < 35:
    print("Your BMI is ", bmi, ", you are obese.")
else:
    print("Your BMI is ", bmi, ", you are clinically obese.")
