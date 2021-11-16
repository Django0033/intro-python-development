bank_accounts = []
balances = []
name = ''
total = 0
will_update = 'yes'


def account_information():
    print()
    print('Account Information:')
    for i in range(len(bank_accounts)):
        bank_account = bank_accounts[i]
        balance = balances[i]
        print(f'{i}. {bank_account} - ${balance}')


print()
print('Enter the names and balances of bank accounts (type: quit when done)')
while name != 'quit':
    name = input('What is the name of this account? ').lower()

    if name != 'quit':
        bank_accounts.append(name.capitalize())
        amount = float(input('What is the balance? '))
        balances.append(amount)

account_information()

print()
for i in balances:
    total += i

average = total / len(balances)

print(f'Total: ${total}')
print(f'Average: ${average:.2f}')
print(
    f'Highest balance: {bank_accounts[balances.index(max(balances))]} - {balances[balances.index(max(balances))]}')

while will_update == 'yes':
    print()
    will_update = input('Do you want to update an account? ').lower()

    if will_update == 'yes':
        index_to_update = int(input(
            'What account index do you want to update? '))
        new_amount = float(input('What is the new amount? '))
        balances[index_to_update] = new_amount

        # You can just indent back this line to print the account information for the two conditions.
        account_information()

    else:
        account_information()
