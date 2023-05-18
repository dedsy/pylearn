# Iterating over a single char in the string:
for char in '123456789':
    print(char + '!')















# Iterating over a single char in the string:
for char in '123456789':
    if char == '2':
        continue
    print(char + '!')











count = 10
while count > 0:
    print(count)
    count = count - 1








# Infinitive loop:
while True:
    users_input = input('Please, input positive number: ')
    if float(users_input) > 0:
        print('Your number is: {0}'.format(users_input))
        break
    else:
        print('{0} is a wrong number.'.format(users_input))





