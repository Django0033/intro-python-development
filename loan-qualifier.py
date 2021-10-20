loan_size = float(input('How large is the loan? 1-10: '))
credit_history = float(input('How good is your credit history? 1-10: '))
income = float(input('How high is your income? 1-10: '))
down_payment = float(input('How large is your down payment? 1-10: '))

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        decision = True
    elif (credit_history >=7 or income >=7) and down_payment >= 5:
        decision = True
    else:
        decision = False
else:
    if credit_history < 4:
        decision = False
    else:
        if income >= 7 or down_payment >= 7:
            decision = True
        elif income >= 4 and down_payment >= 4:
            decision = True
        else:
            decision = False

if decision:
    print('You got the loan!')
else:
    print('Maybe next time...')
