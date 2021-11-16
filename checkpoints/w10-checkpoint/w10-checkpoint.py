shopping_list = []
item = ''

print('Please enter the items of the shopping list (type: quit to finish):')

while item != 'quit':
    item = input('Item: ').lower()

    if item != 'quit':
        shopping_list.append(item.capitalize())

print()
print('The shopping list is:')

for item in shopping_list:
    print(item)

print()
print('The shopping list with indexes is:')

for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f'{i}. {item}')

print()

item_index = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ').lower()
shopping_list[item_index] = new_item.capitalize()

print()
print('The shopping list with indexes is:')

for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f'{i}. {item}')
