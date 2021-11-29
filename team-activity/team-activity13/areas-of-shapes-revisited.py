import math

def compute_area_rectangle(length, width):
    return length * width

def compute_area_square(side):
    return compute_area_rectangle(side,side)

def compute_area_circle(radius):
    return math.pi * radius ** 2

def compute_area(shape, length_radius, width = 1):
    if shape == 'rectangle':
        return compute_area_rectangle(length_radius, width)

    elif shape == 'square':
        return compute_area_square(length_radius)

    elif shape == 'circle':
        return compute_area_circle(length_radius)

    else:
        return 'Invalid shape'

shape_choice = input('Enter shape: ')

if shape_choice == 'rectangle':
    length = int(input('Enter width: '))
    width = int(input('Enter length: '))
    print(compute_area(shape_choice, length, width))

elif shape_choice == 'square':
    side = int(input('Enter side: '))
    print(compute_area(shape_choice, side))

elif shape_choice == 'circle':
    radius = float(input('Enter radius: '))
    print(compute_area(shape_choice, radius))

else:
    print('Invalid shape')

