# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#need to figure out if the number the user chose will come out zero after doing the modulous of 2, because any even number is divided by 2. if the number the user chose comes out to 0 then the number is even, if there is a remainder then the number is odd  
check_num = number % 2

if check_num == 0:
  print("Your number is even")
else:
  print("Your number is odd")




