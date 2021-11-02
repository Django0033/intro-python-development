number_rows_columns = int(input('How many columns and rows do you want in your multiplication table? '))

# When we use range () in the loop below, it will go ug to, but NOT INCLUDING the number
# so here we set the rane_size to be the user's number_rows_columns + 1
range_size = number_rows_columns + 1

for i in range(1, range_size): # This creates rows

    for j in range(1 , range_size): # This prints each number of a row
        product = i * j

product_digits = len(str(product)) # This gets the number of digits of the last product

for i in range(1, range_size): # This creates rows

    for j in range(1 , range_size): # This prints each number of a row
        product = i * j

        if j < number_rows_columns:
            print(f'{product:{product_digits}}', end=' ')

        else:
            print(f'{product:{product_digits}}')
