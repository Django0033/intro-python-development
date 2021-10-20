print()
grade_percentage = float(input('What is your grade percentage? '))
letter = ''
sign = ''

if grade_percentage >= 90:
    letter = 'A'
elif grade_percentage >= 80:
    letter = 'B'
elif grade_percentage >= 70:
    letter = 'C'
elif grade_percentage >= 60:
    letter = 'D'
else:
    letter = 'F'

if (grade_percentage % 10) >= 7 and letter in ('B', 'C', 'D'):
    sign = '+'
elif (grade_percentage % 10) < 3 and grade_percentage < 100 and letter \
        in ('A', 'B', 'C', 'D'):
    sign = '-'

print(f'Your grade is {letter}{sign}.')

if grade_percentage >= 70:
    print('Congratulations! You passed the class.')
else:
    print('You will not pass. Work harder the next time.')
print()

