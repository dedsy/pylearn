# first
if 1 > 0:
    print('1 is greater than 0')








# second
if 1 > 2:
    print('Cannot be!')
else:
    print('1 is less than 2')






# third
if 1 > 2:
    print('Cannot be!')
elif True:
    print('Always true')
else:
    print('Will not be executed')







# Some variables can be poorly initialized:
my_global_var = int(input('Input a number: '))
if my_global_var > 2:
    inner_if_var = 'set'

print(inner_if_var)



if my_global_var != 3:
    this_wont_happen = 'No!'
else:
    but_this_will = 'Yes.'

print(but_this_will)
print(this_wont_happen)  # error here!



# ternary
x = 5
print('Less than zero' if x < 0 else 'Positive or zero')
