# Definition:

empty_tuple = ()
print(empty_tuple)

simple_tuple = (1, 2, 3, 4, 5)
print(simple_tuple)


tuple_with_different_types = (1, 'a', None, True, 2.0)
print(tuple_with_different_types)

# nested:
print((
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
))


# this is a tuple!
this_is_a_tuple = (1,)

# this is not a tuple!
not_a_tuple = (1)








# TUPLES ARE IMMUTABLE!

my_collection = 'abc'
print(my_collection[0])

my_collection[0] = 'z'  # this will error!



my_collection = (1, 2, 3)
print(my_collection[0])

my_collection[0] = 5  # this will error!










# operations

# add
simple_tuple = (1, 2)
simple_tuple = simple_tuple + (3,)
print(simple_tuple)

simple_tuple += (4, )
print(simple_tuple)










# tuple operations:

empty_tuple = ()
tuple1 = (1, 1, 1)
tuple2 = (1, 2)

# indexing:
print(1 in tuple1, 2 in tuple1)

# len:
print(len(tuple1), len(tuple2), len(empty_tuple))

# index access:
print(tuple2[0], tuple1[0:2], tuple1[:-1])








# iteration

for number in (1, 2, 3, 4, 5):
    print('Number is', number)










# unpack:
username, email = ('sobolevn', 'mail@sobolevn.me')
print(username, email)

useful, _ = ('useful', 'this is not used')
print(useful)

# These two examples are impossible:
var1, var2, none_var = (1, 2)
var1, var = (1, 2, 3)
