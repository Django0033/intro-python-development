def compute_area_square(side):
    return side ** 2

square_side = int(input('Enter the length of a side of a square: '))
square_area = compute_area_square(square_side)
print('The area of the square is: {}'.format(square_area))

def compute_area_rectangle(length, width):
    return length * width

rectangle_length = int(input('Enter the length of a rectangle: '))
rectangle_width = int(input('Enter the width of a rectangle: '))
rectangle_area = compute_area_rectangle(rectangle_length, rectangle_width)
print('The area of the rectangle is: {}'.format(rectangle_area))
