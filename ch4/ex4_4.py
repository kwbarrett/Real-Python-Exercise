response = input("What would you like to say> ")
print("You said,'{}'".format(response))

print("Here it is in lowercase: ", response.lower())
print("And again in uppercase: ", response.upper())
print("That is " + str(len(response)) + " characters long.")