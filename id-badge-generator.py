first_name = ''
last_name = ''
email = ''
phone = ''
job = ''
id_number = ''
hair = ''
eyes = ''
month = ''
training = ''

print()
print('Please enter the following information:')
print()
first_name = input('First name: ')
last_name = input('Last name: ') 
email = input('Email adress: ')
phone = input('Phone number: ')
job = input('Job title: ')
id_number = input('ID Number: ')
hair = input('Hair color: ')
eyes = input('Eye color: ')
month = input('What month did you start? ')
training = input('Have you completed advanced training? (Yes / No) ')
print()
print('The ID Card is:')
print('-' * 40)
print(last_name.upper() + ', ' + first_name.capitalize())
print(job.title())
print('ID: ' + id_number)
print()
print(email.lower())
print(phone)
print()
print(f"{'Hair: ' + hair.capitalize():<18} Eyes: {eyes.capitalize()}")
print(f"{'Month: ' + month.capitalize():<18} Training: {training.capitalize()}")
print('-' * 40)
print()
