def convert_cel_to_far(temp_c):
    """Converts a temperature in Celsius to Fahrenheit"""
    temp_fahrenheit = (temp_c * (9 / 5) + 32)
    return temp_fahrenheit


def convert_far_to_cel(temp_f):
    """ Converts a temperature in Fahrenheit to Celsius """
    temp_celsius = (temp_f - 32) * (5 / 9)
    return temp_celsius


userTempF = input("Enter a temperature in degrees F: ")
resultTempC = convert_far_to_cel(float(userTempF))
print(f"{userTempF} degrees F = {resultTempC:.2f} degrees C")

userTempC = input("Enter a temperature in degrees C: ")
resultTempF = convert_cel_to_far(float(userTempC))
print(f"{userTempC} degrees C = {resultTempF:.2f} degrees F")
