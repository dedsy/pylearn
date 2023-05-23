class Array(object):
    def __init__(self, *args):
        self._data = [*args]

    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data)

    def __add__(self, other):
        return self._data + other._data

    def append(self, item):
        self._data += [item]
        return self._data

    def index(self, elem):
        try:
            return self._data.index(elem)
        except ValueError:
            return -1


arr00 = Array()
arr01 = Array(1, 2, 3)


# element by index
print(arr01[2])
# len
print(len(arr01))
# сложение
print(arr00 + arr01)
# append
print(arr00.append(5))
# работа с циклами
for i in arr01:
    print(i)
# index by element
print(arr01.index(2))
