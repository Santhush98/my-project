# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return 3.14159 * radius**2

# Taking user input for the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculating the area of the circle
area = calculate_circle_area(radius)

# Displaying the calculated area
print(f"The area of a circle with radius {radius} is: {area}")

