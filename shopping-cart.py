menu = ['1. Add item', '2. View cart', '3. Remove item', '4. Compute total', '5. Quit']
action = 0

print()
print('Welcome to the Shopping Cart Program!')

while action != 5:
    print()
    print('Please select one of the following:')
    
    for menu_item in menu:
        print(menu_item)

    action = int(input('Please enter an action: '))
