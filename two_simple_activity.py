
#This code is a Python script that demonstrates the use of the random and emoji libraries. It performs two activities 
import random
import emoji
#This First Activity
'''
In the first activity, the code defines a list list1 containing greeting messages.
 It prompts the user to enter their name using the input() function and then uses the random.
 choice() function to select a random greeting message from list1.
 The selected message is concatenated with the user's name and printed to the console.
'''
list1 = ["Hi ", "Hello ","Welcome "]
name = input("Enter Your Name : ")
print(random.choice(list1) + name)

#This second  Activity
'''
In the second activity, the code uses the emoji.emojize() function from the emoji library
 to generate an emoji representation of a yellow heart.
  The name variable is interpolated into the emoji string using an f-string.
   The resulting emoji is printed to the console.
'''
print(emoji.emojize(f"This heart for {name} :yellow_heart:", variant="emoji_type"))
