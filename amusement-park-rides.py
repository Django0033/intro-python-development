class person:
    def __init__(self, age, height):
        self.age = age
        self.height = height

first_rider = person(0,0)
second_rider = person(0,0)

first_rider.age = int(input('What is the age of the first rider? '))

if first_rider.age >= 12 and first_rider.age <= 17:
    golden_pass1 = input('Do you have a golden passport (yes/no)? ').lower()
    if golden_pass1 == 'yes':
        first_rider.age = 18

first_rider.height = int(input('What is the height of the first rider? '))
partner = input('Is there a second rider (yes/no)? ').lower()

if partner == 'yes':
    second_rider.age = int(input('What is the age of the second rider? '))
    if second_rider.age >= 12 and second_rider.age <= 17:
        golden_pass2 = input('Do you have a golden passport (yes/no)? ').lower()
        if golden_pass2 == 'yes':
            second_rider.age = 18
    second_rider.height = int(input('What is the height of the second rider? '))
    if (first_rider.age >= 18 or second_rider.age >= 18) and \
            (first_rider.height >= 36 and second_rider.height >= 36):
        access_granted = True
    elif first_rider.age >= 12 and second_rider.age >= 12 and \
            first_rider.height >= 52 and second_rider.height >= 52:
        access_granted = True
    elif ((first_rider.age >= 14 and second_rider.age >= 16) or \
            (first_rider.age >= 16 and second_rider.age >= 14)) and \
                (first_rider.height >= 36 and second_rider.height >= 36):
        access_granted = True
    else:
        access_granted = False
else:
    if first_rider.age >= 18 and first_rider.height >= 62:
        access_granted = True
    else:
        access_granted = False

if access_granted:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you my not ride.')
