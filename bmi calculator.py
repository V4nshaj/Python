#bmi calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# h=int(height)
bmi = (round)(float(weight)/(float(height)**2))
print(bmi)
if bmi<18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5<=bmi & bmi <25:#and or &
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25<=bmi & bmi<30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30<=bmi & bmi<35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
