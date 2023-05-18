# Step 0:

# Here we define a function:
def this_functions_prints_stars():
    print('I will print stars!')
    print('**********')

# Here we call the function:
this_functions_prints_stars()























# Step 1:
def my_function(input_var1, input_var2):
    print(input_var1, input_var2)
    return input_var1 + input_var2

first_call = my_function(1, 1)
print(first_call)

second_call = my_function(1, 123)
print(second_call)
















# Step 3:
def function_with_default_value(name, age=0, needs_stars=False):
    message = '{0} is {1} years old!'.format(name, age)
    print(message)
    if needs_stars:
        print('*****')

function_with_default_value('Nikita')
function_with_default_value('Alex', 19)
function_with_default_value(name='Bob', age=40, needs_stars=True)






def func_with_kw(arg1, *, arg2):
    print(arg1, arg2)

func_with_kw(1, 2)
func_with_kw(1, arg2=2)
func_with_kw(arg1=1, arg2=2)


def func_with_pos(arg1, /, arg2):
    print(arg1)

func_with_kw(1, arg2=2)
func_with_kw(arg1=1, arg2=2)


x = 1
def func_with_all(
    arg_named_or_pos,
    arg_with_default=None,
):
    my_int = 2  # const / let / var
    print(int('1'))












# Step 4:
def named_values(name=None, surname=None, patronimic=None):
    print('Full name: {0} {1} {2}'.format(surname, name, patronimic))

named_values(name='Nikita', surname='Sobolev', patronimic='Andreevich')
named_values(surname='Petrov', patronimic='Ivanovich', name='Ivan')
named_values(surname='Semenov', name='Petr', patronimic='Ivanovich')
