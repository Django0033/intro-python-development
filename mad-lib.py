adjective = ''
adjective2 = ''
adjective3 = ''
adjective4 = ''
adjective5 = ''
animal = ''
animal2 = ''
exclamation = ''
verb = ''
verb2 = ''
verb3 = ''
verb4 = ''
verb5 = ''
def noun_check(noun):
    noun_prefixed = ''
    if noun[0] in ('a', 'e', 'i', 'o', 'u'):
        noun_prefixed = 'an ' + noun
        return noun_prefixed
    else:
        noun_prefixed = 'a ' + noun
        return noun_prefixed

print()
print('Please enter the following:')
print()
adjective = input('adjective: ')
animal = input('animal: ')
verb = input('verb: ')
exclamation = input('exclamation: ')
verb2 = input('verb: ')
verb3 = input('verb: ')
adjective2 = input('adjective: ')
adjective3 = input('adjective: ')
adjective4 = input('adjective: ')
adjective5 = input('adjective: ')
animal2 = input('animal: ')
verb4 = input('verb: ')
verb5 = input('verb: ')
print()
print('Your story is:')
print()
print('The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all ')
print(f'I could think to do was to {verb2.lower()} over and over. Miraculously,') 
print(f'that caused it to stop, but not before it tried to {verb3.lower()}') 
print(f'right in front of my family.')
print()
print(f'My family decided to {verb4.lower()} the {animal.lower()}. It was very {adjective2.lower()}! The {animal.lower()}')
print(f'started to {verb5.lower()} all over the house. My father said "that\'s because it is a')
print(f'little bit {adjective3.lower()}", so he brought {noun_check(animal2.lower())} as a companion for the')
print(f'{animal.lower()}. I thought it was {noun_check(adjective4.lower())} idea. Now we have a pretty {adjective5.lower()}')
print(f'family with {noun_check(animal.lower())}, {noun_check(animal2.lower())}, my parents and I.')
print()
