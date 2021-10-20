def desition(question, option1, option2, option3):
    answer = input(f'{question} {option1}/{option2}/{option3}: ').lower()
    if answer == option1.lower():
        choice = 'choice1'
        return choice
    elif answer == option2.lower():
        choice = 'choice2'
        return choice
    elif answer == option3.lower():
        choice = 'choice3'
        return choice
    else:
        choice = 'no_choice'
        return choice

def path(choice, path1, path2, path3):
    if choice == 'choice1':
        print(f'{path1}')
    if choice == 'choice2':
        print(f'{path2}')
    if choice == 'choice3':
        print(f'{path3}')

print()
print()
print('         #############################')
print('         #                           #')
print('         #       For the Kingdom     #')
print('         #                           #')
print('         #############################')
print()
print()
print('The orcs are terrorizing your people. ')
print('You, the King of Fiomar, have the power to save your kingdom.')
print()
choice = desition('Do you want to start your adventure?', 'YES', 'NO', '')
# desition('Do you want to start your adventure?', 'YES', 'NO', '')
print(choice)
# if answer == 'yes':
    # print('Here you will start your adventure.')
print()
