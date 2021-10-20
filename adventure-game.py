print()
print()
print('         #############################')
print('         #                           #')
print('         #      For the Kingdom      #')
print('         #                           #')
print('         #############################')
print()
print()
print('The orcs are terrorizing your people. ')
print('You, the King of Fiomar, have the power to save your kingdom.')
print()

while True:
    answer = input('Do you want to start your adventure? YES/NO: ').lower()
    if answer not in ('yes', 'no'):
        print('Please, chose a valid option')
        print()
        continue
    else:
        break

if answer == 'yes':
    print()
    print('Here you will start your adventure.')
elif answer == 'no':
    print()
    print('Perhaps your people can handle this. Just go back to sleep.')
