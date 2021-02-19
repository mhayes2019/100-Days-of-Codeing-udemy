#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

#first you need to import the random module
import random
#need to use the random.randint in order to get a random number from 0 to 1 because 0 is tails and 1 is heads
random_choice = random.randint(0,1)


user_choice = input("Please choose 'Heads' or 'Tails' ").capitalize()

if user_choice == "Heads":
  user_num = 1
else:
  user_num = 0
if user_num == random_choice:
  print("You got it correct")
else:
  print("Sorry you got it wrong")











