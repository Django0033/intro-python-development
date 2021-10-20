print()
first_number = float(input('Enter a number: '))
second_number = float(input('Enter a second number: '))
print()

if first_number > second_number:
    print('The first number is greater')
else:
    print('The first number is not greater')
    
if first_number == second_number:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if first_number < second_number:
    print('The second number is greater')
else:
    print('The second number is not greater')
print()

my_favorite_animal = 'lion'
user_favorite_animal = input('What is your favorite animal? ')

if my_favorite_animal == user_favorite_animal.lower():
    print('That\'s my favorite animal too!')
else:
    print('That one is not my favorite.')
print()
