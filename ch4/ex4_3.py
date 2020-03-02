# 1. Write a script that converts the following strings to lowercase: "Animals",
# "Badger", "Honey Bee", "Honeybadger". Print each lowercase
# string on a separate line.
string1 = "Animals"
string2 = "Badger"
string3 = "Honey Bee"
string4 = "Honeybadger"

print(string1.lower())
print(string2.lower())
print(string3.lower())
print(string4.lower())

# 2. Repeat Exercise 1, but convert each string to uppercase instead of
# lowercase.
print(string1.upper())
print(string2.upper())
print(string3.upper())
print(string4.upper())

# 3. Write a script that removes whitespace from the following strings:
# Print out the strings with the whitespace removed.
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

# 4. Write a script that prints out the result of .startswith("be") on each
# of the following strings:

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

# 5. Using the same four strings from Exercise 4, write a script that
# uses string methods to alter each string so that .startswith("be")
# returns True for all of them.

print(string1.lower().startswith("be"))
print(string2.startswith("be"))
print(string3.lower().startswith("be"))
print(string4.lower().lstrip().startswith("be"))
