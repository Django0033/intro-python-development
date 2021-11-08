friends = []
friend = ''

while friend.lower() != 'end':
    friend = input('Type the name of a friend: ')
    if friend.lower() != 'end':
        friends.append(friend)
    else: 
        break

print()
print('Your friends are:')

for friend in friends:
    print(friend)
