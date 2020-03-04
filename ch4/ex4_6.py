# 1. Create a string containing an integer, then convert that string into
# an actual integer object using int(). Test that your new object is
# a number by multiplying it by another number and displaying the
# result.
word = "49"
print(int(word)* 2)

# 2. Repeat the previous exercise, but use a floating-point number and
# float().
print(float(word) * 2)

# 3. Create a string object and an integer object, then display them sideby-
# side with a single print statement by using the str() function.
my_string = "50"
my_integer = 50
print(my_string + " " + str(my_integer))

# 4. Write a script that gets two numbers from the user using the
# input() function twice, multiplies the numbers together, and
# displays the result. If the user enters 2 and 4, your program should
# print the following text:
# The product of 2 and 4 is 8.0.

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

print(f"The product of {num1} and {num2} is {float(num1) * float(num2)}")
