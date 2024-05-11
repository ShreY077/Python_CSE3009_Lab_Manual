import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

# Accept radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate area
area = calculate_circle_area(radius)

# Print the area
print("The area of the circle with radius", radius, "is:", area)
