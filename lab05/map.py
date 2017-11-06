# Task 3
# Creating a temperature list, in celsius
temp_list = [12,11,10,9,14]

# Fahrenheit: Convert temperatures that are in Celsius to Fahrenheit
# Input: Temperature list in Celsius
# Output: List of temperatures in Fahrenheit
def fahrenheit (c):
# Formula of converting Celsius to Fahrenheit
    return (c * (9 / 5) + 32)
newtemps = map (fahrenheit, temp_list)
print newtemps