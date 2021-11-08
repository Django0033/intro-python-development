numbers = []
number = ''
number_sum = 0

print('Enter a list of numbers, type 0 when finished.')

while number != 0:
    print('While number is not equal to 0...')
    number = float(input('Enter number: '))

    if number != 0:
        numbers.append(number)

for number in numbers:
    number_sum += number

print(numbers)
print(number_sum)
