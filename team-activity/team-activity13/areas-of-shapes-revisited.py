import math

def compute_area_rectangle(length, width):
    return length * width

def compute_area_square(side):
    return compute_area_rectangle(side,side)

def comute_area_circle(radius):
    return math.pi * radius ** 2

square_side = int(input('Enter the length of a side of a square: '))
square_area = compute_area_square(square_side)
print('The area of the square is: {}'.format(square_area))

rectangle_length = int(input('Enter the length of a rectangle: '))
rectangle_width = int(input('Enter the width of a rectangle: '))
rectangle_area = compute_area_rectangle(rectangle_length, rectangle_width)
print('The area of the rectangle is: {}'.format(rectangle_area))

circle_radius = int(input('Enter the radius of a circle: '))
circle_area = comute_area_circle(circle_radius)
print('The area of the circle is: {}'.format(circle_area))
