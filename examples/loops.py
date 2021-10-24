tip = float(input('What is the tip amount? '))

while tip < 0:
    print('Sorry, the tip cannot be negative')
    tip = float(input('What is the tip amount? '))
    # Jump back up to line 3

print(f'You have tipped an amount of ${tip:.2f}')

# The variable must be initialized with a value that access the loop
# The variables must be declared outside the loop
# The standard initialization value is 0
number = 0

# Keep looping as long as the number is less than or equal to 5
while number <= 5:
    # Display the number
    print(f'The number is: {number}')

    #Update the number to be one more than it was
    number = number + 1

print('Finished with the loop')
