import math


# Challenge 2
single_length = float(input('I need a real challenge, give me just one length! '))
square_area = single_length ** 2
circle_area = math.pi * single_length ** 2
cube_volume = square_area * single_length
sphere_volume = 4 * math.pi * single_length ** 2
print(f'The area of the square is: {square_area}')
print(f'The area of the circle is: {circle_area}')
print(f'The volume of the cube is: {cube_volume}')
print(f'The volume of the sphere is: {sphere_volume}')
print()

# Challenge 3
square_side = float(input('What is the length of a side of the square in centimeters? '))
square_area_cm = square_side ** 2
square_area_m = square_area_cm / 10000
print(f'The area of the square is: {square_area_cm} square centimeters or')
print(f'{square_area_m} square meters')
rectangle_length = float(input('What is the length of rectangle? '))
rectangle_width = float(input('What is the width of rectangle? '))
rectangle_area = rectangle_length * rectangle_width
print(f'The area of the rectangle is: {rectangle_area}')
circle_radius = float(input('What is the radius of the circle? '))
circle_area = math.pi * circle_radius ** 2
print(f'The area of the circle is: {circle_area}')


