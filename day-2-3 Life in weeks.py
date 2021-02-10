# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#need to get the age of the user and convert it into an interger
user = int(age)

#need to assign a variable to how many years the user has left from 90 years and
years_remaining = 90 - user

# in order to get the days remainig, you need to take the years remaining from the user and times it by 365 beause there are 365 days in a year and assign that to a new variable
days_remaining = years_remaining * 365 

#in order to get the weeks remaining, you need to take the years remaining from the user and times it by 52 because there are 52 weeks in a year and assign that to a new variable 
weeks_remaining = years_remaining * 52

#in orer to get the months_remaining, you need to take the years remaining from the user and times is by 12 because there are 12 months in a year and assign that to a new variable 
months_remaining = years_remaining * 12

#need to use the f-string to allow the combination of data types such as the strings and integers to be used together without having to do conversions
print(f'You have {days_remaining} days,{weeks_remaining} weeks,and {months_remaining} months left')









