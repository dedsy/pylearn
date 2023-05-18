# Complex step 1:
def factorial(n):  # This function is recursive, it calls itself.
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))  # 4 * 3 * 2 * 1 = 24

















# Complex step 2:
def do_callback(function, argument):  # you can pass functions as an arguments
    return function(argument)  # this is called "callback"

result = do_callback(len, 'string')
print(result)

















# Complex step 3:
def enclosing(value):
    def _inner():
        print('value: {value}, new_value: {new_value}'.format(
            new_value=new_value, value=value,
        ))
    new_value = str(value * 10) * 2
    _inner()
    return new_value

enclosing(25)
