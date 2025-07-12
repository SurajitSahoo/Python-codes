# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# List of temperatures in Celsius
celsius_temperatures = [0, 10, 20, 30, 40]

# Convert each temperature in the list to Fahrenheit
fahrenheit_temperatures = [celsius_to_fahrenheit(temp) for temp in celsius_temperatures]

# Output the result
print("Celsius temperatures:", celsius_temperatures)
print("Fahrenheit temperatures:", fahrenheit_temperatures)
