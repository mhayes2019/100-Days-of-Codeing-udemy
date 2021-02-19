# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#first need to import the random module
import random

#was not allowed to use .choice() so had to google another way to do it
#came up with random.sample()
#created another variable payer to place random.sample into and the arguments that I stored inside was the names (for the names in the group) and k=1 (by using this it allows you to specify how many random names you want pulled from the names list)
payer = random.sample(names, k=1)
print(f'{payer} will be paying the bill today')



