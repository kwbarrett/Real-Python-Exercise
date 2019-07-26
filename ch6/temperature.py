def convert_cel_to_far(tempC):
    """Converts a temperature in Celsius to Fahrenheit"""
    tempF = (tempC * (9/5) + 32 )
    return tempF
    
def convert_far_to_cel(tempF):
    """ Converts a temperature in Fahrenheit to Celsius """
    tempC = (tempF - 32) * (5/9)
    return tempC
    
userTempF = input("Enter a temperature in degrees F: ")
userTempC = input("Enter a temperature in degrees C: ")

resultTempC = convert_far_to_cel(float(userTempF))
resultTempF = convert_cel_to_far(float(userTempC))

print(f"{userTempF} degrees F = {resultTempC:.2f} degrees C")
print(f"{userTempC} degrees C = {resultTempF:.2f} degrees F")
    