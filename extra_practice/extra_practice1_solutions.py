#Prompt 1:
# Write a program that adds 3 to a variable and prints the new value. 
# The variable should be initialized to 12 before 3 is added to it.
# Bonus: Can you think of another way to write this? 
# Possible Solution 1a:
var1 = 12
var1 = var1 + 3
print(var1) 
# Possible Solution 1b:
var1 = 12
var1 += 3
print(var1) 

#Prompt 2:
# Write a program that squares a variable and prints the new value. 
# The variable should be initialized to 5 before it is squared.
# Bonus: Can you think of another way to write this? 
# Possible Solution 2a:
var2 = 5
var2 *= var2
print(var2) 
# Possible Solution 2b:
var2 = 5
var2 **= 2
print(var2) 

#Prompt 3:
# Write a program that compares two numbers and prints whether or not the first number is greater than the second number.
# You can test your program using different numbers.
# Bonus: Can you make the program print "is greater" when the first number is greater and print "is smaller" when the first is smaller. 
# Possible Solution 3a:
a = 7
b = 5
print(a > b) 
# Possible Solution 3b:
a = 7
b = 5
if a > b:
    print('is greater')
else:
    print('is smaller')

#Prompt 4:
# Write a program that prints whether or not a number is divisble by 5.
# You can test your program using different numbers.
# Bonus: Can you make the program print "yes" is the number is divisible and "no" if the number isn't divisible?
# Possible Solution 4a:
var4 = 4
print(var4 % 5 == 0)
# Possible Solution 4b:
var4 = 4
if var4 % 5 == 0:
    print('yes')
else:
    print('no')

#Prompt 5:
# Write a program that implements this equation: 5x + 2
# x is a varible and that you can assign different values to in order to test your program.
# Example Outputs --
#   when x is 3, 5(3) + 2 = 17, the output is 17
#   when x is 2, 5(2) + 2 = 12, the output is 12
# Bonus: Can you implement this equation: (5x + 2)^2?
# Example Outputs --
#   when x is 3, (5(3) + 2)^2 = 289, the output is 289
#   when x is 2, (5(2) + 2)^2 = 144, the output is 144
# Possible Solution 5a:
x = 3
print(5*x + 2)
# Possible Solution 5b:
x = 3
print((5*x + 2)**2)