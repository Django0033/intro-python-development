menu = ['1. Add item', '2. View cart',
        '3. Remove item', '4. Compute total', '5. Quit']
action = 0
shopping_cart = []
prices = []
total = 0

print()
print('Welcome to the Shopping Cart Program!')

while action != 5:
    print()
    print('Please select one of the following:')

    for menu_item in menu:
        print(menu_item)

    action = int(input('Please enter an action: '))

    if action == 1:
        item = input('What item would you like to add? ').lower()
        shopping_cart.append(item.capitalize())
        price = float(input(f'What is the price of \'{item.capitalize()}\'? '))
        prices.append(price)
        print(f'\'{item.capitalize()}\' has been added to the cart.')

    elif action == 2:
        print('The contents of the shopping cart are:')
        align = len(item)

        for item in shopping_cart:

            if len(item) > align:
                align = len(item)

        for i in range(len(shopping_cart)):
            item = shopping_cart[i]
            price = prices[i]
            print(f'{i + 1}. {item:{align}} - {price:.2f}')

    elif action == 3:
        index_to_remove = int(
            input(f'Which item would you like to remove? ')) - 1
        shopping_cart.pop(index_to_remove)
        prices.pop(index_to_remove)
        print('Item removed.')

    elif action == 4:

        for price in prices:
            total += float(price)

        print(
            f'The total price of the items in the shopping cart is: ${total:.2f}')

print('Thank you. Goodbye.')
