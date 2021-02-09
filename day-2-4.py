#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator")

user_bill = input("What was the total bill? $")

user_percentage = input("Which percentage tip would you like to give? 10, 12 or 15? ")

user_split = input("How many people are you splitting the bill with? ")

#in order to get the percentage we need to take the users choice of percentage and divide it by 100 also need to convert it into an integer 
user_tip_percentage = int(user_percentage) / 100 

#after we get the percentage choice of the user we need to take the bill amount and times it by the users percentage choice 
user_bill_with_percentage = float(user_bill) * float(user_tip_percentage)

#next we need to add the users bill to the percentage amount 
total_bill = float(user_bill) + float(user_bill_with_percentage)

#in order to split the bill with the amount of people in the party we need to divide the total_bill after the percentage was added and divide it to the amount of people 
new_total_bill = float(total_bill) / int(user_split)

#assignment calls for the decimal to be rounded two places so here the round() is used and it is calling to move 2 spaces 
final_total_bill = round (new_total_bill, 2)

#print out final message to user using the  f-string 
print(f'Your bill split {user_split} ways will be ${final_total_bill} each person')
