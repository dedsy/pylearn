# Definition:

empty_list = []
print(empty_list)

simple_list = [1, 2, 3, 4, 5]
print(simple_list)


list_with_different_types = [1, 'a', None, True, 2.0]
print(list_with_different_types)

# nested:
print([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])







my_collection = [1, 2, 3]
print(my_collection, my_collection[0])

my_collection[0] = 5  # this will work :)
print(my_collection)






# operations

# add
my_list = [1, 2]
my_list.append(3)
print(my_list)

# pop
my_list.pop(0)  # by index
print(my_list)

# remove
my_list.remove(3)  # by value
print(my_list)



# indexing:
has_three = [3]
print(3 in has_three, 2 in has_three)

# len:
empty_list = []
list_with_two_items = [1, 2]
big_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(empty_list), len(list_with_two_items), len(big_list))

# index access:
print(big_list[0], big_list[0:2], big_list[:-1])







# lists from tuple vs tuples from lists:
my_tuple = (1, 2)
my_list = [1, 2]

print(my_list == my_tuple)

print(list(my_tuple) == my_list)
print(my_tuple == tuple(my_list))







# unpack
movie, year = ['Star Wars', 2005]
print(movie, year)











# generating lists: range() function
# xrange in 2.7 = range in 3
print('range', list(range(1, 10)))

for i in list(range(1, 15, 2)):
    print(i)
