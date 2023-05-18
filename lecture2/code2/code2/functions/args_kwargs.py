# Function can receive unlimited number of positional arguments

def sum_all(*args):
    print(args, type(args))
    result = 0
    for arg in args:
        result += arg
    return result

print(sum_all(1, 2, 3, 4, 5, 6, 7))

















# Functions can receive unlimited number of keyword arguments

def build_dict(**kwargs):
    print('A lot of keyword arguments', kwargs)
    print('kwargs is a dict', type(kwargs))
    return dict(**kwargs)

build_dict(any_possible=None, values=[], you_wish=1)

















# Function that will cover 100% of arguments

def send_anything(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)

send_anything(1, 15, 'a', value=True, other=5, new_value=False)
