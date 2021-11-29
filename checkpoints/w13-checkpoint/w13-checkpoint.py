def display_regular(same_message):
    return same_message

def display_upper(same_message):
    return same_message.upper()

def display_lower(same_message):
    return same_message.lower()

message = input('What is your message? ')
same_message = display_regular(message)
print(same_message)
same_message = display_upper(message)
print(same_message)
same_message = display_lower(message)
print(same_message)
