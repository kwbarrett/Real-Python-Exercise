for i in range(2,11):
    print(i)

n = 2
while n <= 10:
    print(n)
    n += 1
    
def doubles(num):
    """Returns a value that is 2* the supplied argument"""
    return num * 2

myNum = 2
for x in range(3):
    myNum = doubles(myNum)
    print(myNum)