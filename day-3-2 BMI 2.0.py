# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#assigment calls to round the result to the nearest whole number so need to use the round() function
bmi = round(weight / height ** 2)

#anything under 18.5
if bmi <18.5:
  print(f"Your bmi is {bmi}, you are underweight")
#anything between 18.6 and less than 25
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight")
#anything between 25 and 29
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
#anything between 30 and 34
elif bmi < 35:
  print (f"Your bmi is {bmi}, you are obese")
#anything 35 and above
else:
    print("You are clinically obese")




