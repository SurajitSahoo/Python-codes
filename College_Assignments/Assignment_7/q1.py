import math

# Function to calculate area and circumference
def calculate_circle_properties(radius):
    # Area of circle = π * radius^2
    area = math.pi * radius ** 2
    
    # Circumference of circle = 2 * π * radius
    circumference = 2 * math.pi * radius
    
    return area, circumference

# Input: radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Get the area and circumference
area, circumference = calculate_circle_properties(radius)

# Output the results
print(f"The area of the circle with radius {radius} is: {area:.2f}")
print(f"The circumference of the circle with radius {radius} is: {circumference:.2f}")
