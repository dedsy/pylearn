# Local scope

def scoped_function(arg):
    value = arg * 10
    print(value)

scoped_function(2)




















# Returning something

def return_some(input_value):
    calc = input_value - 7
    print(calc)
    return calc

print(return_some(4))
















# Global scope

SOME_VAR = 'value'

def print_var():
    print(SOME_VAR)

print_var()










# You cannot modify global scope

SOME_VAR = 'value'

def modify_var():
    SOME_VAR += '_extra'  # this will error!

modify_var()
print(SOME_VAR)














# But you can mutate it

GLOBAL_LIST = []

def append_to_list(item):
    print('Adding', item)
    GLOBAL_LIST.append(item)

append_to_list(1)
append_to_list(2)
print(GLOBAL_LIST)











# You can modify global scope with `global`

SOME_VAR = 'value'


def modify_var():
    global SOME_VAR
    SOME_VAR += '_extra'  # this will error!

modify_var()
print(SOME_VAR)

# Let's try again!
modify_var()
print(SOME_VAR)


