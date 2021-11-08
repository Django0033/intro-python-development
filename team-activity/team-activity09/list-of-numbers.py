numbers = []
number = ''
number_sum = 0

print('Enter a list of numbers, type 0 when finished.')

while number != 0:
    number = float(input('Enter number: '))

    if number != 0:
        numbers.append(number)

for number in numbers:
    number_sum += number

number_average = number_sum / len(numbers)

print(f'The sum is: {int(number_sum)}')
print(f'The average is: {number_average}')
print(f'The largest number is: {max(numbers)}')
