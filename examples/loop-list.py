items = ['crayon', 'scissors','paper', 'glitter glue', 'markers', 'pens']

for item in items:
    print(f'The item is: {item}')

# Looping through numbers
# Range returns a list of numbers up but not including 10
for number in range(10):
    print(number)

# This loop will start with 100, and go up to, but not including 200
for i in range(100, 200):
    print(i)

# This loop will do the same thing, but this time, it wil count by 10
for i in range(100, 200, 10):
    print(i)

# The inner loop is run every time the outer loop runs
for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f'--{j}')

