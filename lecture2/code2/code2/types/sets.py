empty_set = set()
my_set = {1, 2}

set_with_different_types = {1, False, None, ''}
print(set_with_different_types)

# Collision:
collision = {1, True, 1.0}
print(collision)








# operations:

# add
my_set = {1, 2, 3}
my_set.update({4, 5})
print(my_set)


# union vs intersection
first = {1, 2, 3}
second = {3, 4, 5}

print(first.union(second))
print(first.intersection(second))










# cannot access by index:
my_set = {1, 2, 3}
print(my_set[0])  # this will error!













# search is fast!
my_set = {1, 2, 3}

print(1 in my_set)
print(9 in my_set)
