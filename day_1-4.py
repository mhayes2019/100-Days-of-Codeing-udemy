# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#we use a temp variable to hold the value of a, so when the value of a is overwritten by b we have the backup of a which we later assign to b 
temp = a 
a = b
b = temp

#Another Way without using a temp variable
#a,b = b,a



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


