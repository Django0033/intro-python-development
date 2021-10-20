print()
child_meal_price = float(input('What is the price of a child\'s meal? '))
adult_meal_price = float(input('What is the price of a adult\'s meal? '))
drink_price = float(input('What is the price of a drink? '))
appetizer_price = float(input('What is the price of an appetizer? '))
children = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
drinks = int(input('How many drinks did they take? '))
appetizer = int(input('How many appetizers did they take? '))
tax = float(input('What is the sales tax rate? '))
tip_percentage = float(input('What is the tip percentage? '))

child_subtotal = child_meal_price * children
adult_subtotal = adult_meal_price * adults
drink_subtotal = drink_price * drinks
appetizer_subtotal = appetizer_price * appetizer
subtotal = child_subtotal + adult_subtotal + drink_subtotal + appetizer_subtotal
sales_tax = subtotal * tax / 100
tip = subtotal * tip_percentage / 100
total = subtotal + sales_tax + tip

print()
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Tip: ${tip:.2f}')
print(f'Total: ${total:.2f}')
print()
payment_amount = float(input('What is the payment amount? '))
change = payment_amount - total
print(f'Change: ${change:.2f}')
print()
