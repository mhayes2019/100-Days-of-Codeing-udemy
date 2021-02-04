#Creating a BMI Calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#need to figure out the euqation to get your bmi which is weight / height to the 2nd power. 
#that equation can get assigned to a variable (bmi)
#need to convert the weight and the height into an integer and a float because when it gets inputted it will get inputted as a string because it came from the user

bmi = int(weight) / float(height) ** 2

#next, in order to turn it the answer into an int as the assigment is asking we need to assign the bmi to an int and assign it to a new variable (new_bmi)
new_bmi = int(bmi)

#then we print
print(new_bmi)












