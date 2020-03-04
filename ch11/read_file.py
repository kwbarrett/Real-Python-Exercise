input_file = open("hello.txt", "r")

for line in input_file.readlines():
    print(line, end="")

input_file.close()