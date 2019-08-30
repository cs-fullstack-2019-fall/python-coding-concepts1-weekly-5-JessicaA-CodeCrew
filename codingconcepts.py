# 1
# # Problem 1:
# # Ask a user for the year they were born by calculating their age. Assuming they already had their birthday and it’s 2019 print “You are [AGE] years old”
#
# userInput = int(input("What year were you born?:  "))
# currentYear = 2019
# userAge = (currentYear - userInput)
# print(userAge)
#
# # Problem 2:
# # Ask the user for a string. If they enter “Kenn”, “Kevin”, “Erin”, or “Autumn” print “Hello Teacher”. Otherwise print “Hello Student”
#
# userInput1 = input("Enter a name:  ")
#
# if userInput1 == ("Kenn", "Kevin", "Erin", "Autumn"):
#     print("Hello Teacher")
# else:
#     print("Hello Student")
#
# # Problem 3:
# # Ask the user for a negative number. Print from 7 down to the user's negative number. You must include the user's number.
#
# askUserNeg = int(input("Enter a negative number:  "))
# if askUserNeg <=
#
# # Problem 4:
# # Ask the user to enter a number between -10 to -5. If their input is not between the two numbers ask them to do it again until they get it right. Afterward they print the correct number, print "Good job".
#
userNumber = int(input("Enter a number between -10 and -5:   "))
if userNumber <= -10:
    print ("Try Again")
else:
    print("Good Job")


# # Problem 5:
# # Create the list: squad = ["One", "Two", "Three", "Four", "Five"]. Print the list in reverse without using a list method.
#
squad = ["One", "Two", "Three", "Four", "Five"]



# Problem 6:
# Create a function that will have the string firstName as a parameter. In the function ask the user for their last name. Print "Hello [FIRST & LAST NAME]" in the function. Call that function.

def nameFunc(firstName):
    lastName = input("Enter you last name:  ")
