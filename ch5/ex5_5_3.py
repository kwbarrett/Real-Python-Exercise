myNum1 = float(input("Enter a number: "))
myNum2 = float(input("Enter another number: "))

result = myNum1 - myNum2

print(f"The difference between {myNum1} and {myNum2} is an integer? {result.is_integer()}!")