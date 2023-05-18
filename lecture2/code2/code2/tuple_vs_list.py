# LISTS ARE MUTABLE!

my_collection = 'abc'
print(my_collection[0])

my_collection[0] = 'z'  # this will error!



my_collection = (1, 2, 3)
print(my_collection[0])

my_collection[0] = 5  # this will error!



my_collection = [1, 2, 3]
print(my_collection[0])

my_collection[0] = 5  # this will work :)
