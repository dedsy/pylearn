class Array(object):
    def __init__(self, *args):
        self._data = [*args]

    # Добавляет элемент в конец списка
    def add(self, item):
        self._data.append(item)
        return self._data

    # Получаем index элемента, если нет указанного элемента возвращаем -1
    def index(self, item):
        try:
            _ind = self._data.index(item)
            return _ind
        except ValueError:
            return -1

    # Получаем длину
    def len(self):
        return len(self._data)

    # Возвращаем весь список
    def result(self, index=None):
        return self._data

    # Поиск элемента по индексу, с валидацией существования указанного индекса,
    # типа аргумента (int) и наличие самого аргумента
    def elem_by_index(self, index=None):
        if index is not None:
            try:
                return self._data[index]
            except IndexError:
                return 'Элемента с таким индексом не существует!'
            except TypeError:
                return 'Индекс может быть только int!'
        else:
            return 'Нет обязательного аргумента!'


# Создание
arr01 = Array()
arr02 = Array(1)
arr03 = Array(1, 2, 3)

# Добавление
print('Результат добавление объекта к классу: {0}'.format(arr02.add(42)))

# Длина
print('Длина: {0}'.format(arr02.len()))

# Сложение
print('Сложение: {0}'.format(arr02.result() + arr03.result()))

# Index объекта
print('Индекс объекта: {0}'.format(arr02.index(5)))

# Цикл
for i in arr02.result():
    print(i)

# Получать значение по индексу
print('Получение значения по индексу: {0}'.format(arr02.elem_by_index()))
