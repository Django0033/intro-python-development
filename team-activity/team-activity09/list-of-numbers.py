numbers = []
number = ''
number_sum = 0
positive_numbers = []

print()
print('Enter a list of numbers, type 0 when finished.')

while number != 0:
    number = float(input('Enter number: '))

    if number != 0:
        numbers.append(number)

for number in numbers:
    number_sum += number

    if number > 0:
        positive_numbers.append(number)

number_average = number_sum / len(numbers)

print(f'The sum is: {int(number_sum)}')
print(f'The average is: {number_average}')
print(f'The largest number is: {max(numbers)}')
print(f'The smallest positive number is: {int(min(positive_numbers))}')

numbers.sort()

print('The sorted list is:')

for number in numbers:
    print(int(number))
