def compute_area_square(side):
    return side ** 2

square_side = int(input('Enter the length of a side of a square: '))
square_area = compute_area_square(square_side)
print('The area of the square is: {}'.format(square_area))
