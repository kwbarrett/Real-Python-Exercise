data = ((1,2),(3,4))

for row in range(len(data)):
    print(f"Row {row+1} sum {data[row][0] + data[row][1]}")

numbers = [4,3,2,1]
numbers_copy = numbers[:]
numbers.sort()
print(f"numbers = {numbers}")
print(f"numbers_copy = {numbers_copy}")