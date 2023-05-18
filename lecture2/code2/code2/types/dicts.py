empty_dict = {}

this_is_dict = {'key': 'value'}
nested_dict = {
    'people': {
        'Nikita': 1,
        'Sveta': 2,
        'Stepan': 0,
    }
}


# Be careful!
this_is_set = {'key', 'value'}
print(this_is_set == this_is_dict)












# DICTS ARE MUTABLE!
var = {1: 'value'}
var.update({2: 'new value'})
print(var)


var[1] = 'mutated value'
print(var)








# operations with dicts:

# add:
hero = {}
hero.update({'name': 'Super Mario'})
print(hero)

# get:
print(hero['name'])
print(hero.get('job', 'plumber'))

# get only keys:
print(hero.keys())

# get only values:
print(hero.values())

# remove:
test_dict = {'pop-by-key': 1}
popped = test_dict.pop('pop-by-key')
print(popped)













# iterate:
to_iterate = {1: 'x2', 2: 'x4', 3: 'x8'}
for key in to_iterate:
    print(key, to_iterate[key])

for key, value in to_iterate.items():
    print(key, value)

