def invest(amount, rate, years):
    principal = amount
    for x in range(1,(years+1)):
        principal = principal  + (principal * rate)
        print(f"Year {x} ${principal:,.2f}")


amount = float(input("Enter an amount: "))
return_rate = float(input("Enter a rate of return: "))
years = int(input("Enter term: "))

result = invest(amount, return_rate, years)