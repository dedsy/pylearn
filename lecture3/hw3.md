## Теория

Порядок прочтения важен!

### ООП в целом

- Начальный уровень теории: https://habrahabr.ru/post/87119/
- Принципы ООП: https://habrahabr.ru/post/87205/

### ООП и Python

- Основы: https://pythonworld.ru/osnovy/obektno-orientirovannoe-programmirovanie-obshhee-predstavlenie.html
- Примеры использования: http://snakeproject.ru/rubric/article.php?art=python_oop
- Большая теоритическая статья: https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
- Магические методы: https://rszalski.github.io/magicmethods/

### Критика

- Почему в некоторых случаях не нужен ООП: https://habrahabr.ru/post/140581/
- Сомнение в принципах ООП: https://habrahabr.ru/post/147927/

### Детали реализации

- super: http://pythonicway.com/education/python-oop-themes/21-python-inheritance и https://www.youtube.com/watch?v=EiOglTERPEo
- Магические методы: https://habrahabr.ru/post/186608/
- class attributes vs instance attributes: http://stackoverflow.com/questions/207000/python-difference-between-class-and-instance-attributes


## Практика

Написать свой собственный класс "списков", который мы назовем `Array`.

Что должен делать уметь ваш `Array`?

- Создавать себя как на примере: `Array()` - пустой списо, `Array(1)` = список из одного объекта `1`, `Array(1, 2, 3)` - список из трех объектов. `Array` должен уметь работать с любым количеством аргументов
- Добавлять новый объект внутрь списка через метод `.append()`
- Складываться с другими `Array`. Например: `Array(1) + Array(2) == Array(1, 2)`
- Узнавать свою длину через функцию `len()`
- Находить индекс переданного объекта через метод `.index()`, возвращаем `-1`, если такого объекта в списке нет. Например: `Array('a', 'b').index('b') == 1`
- Работать с циклом `for`: `for element in Array(1, 2, 3):`
- Получать значение по индексу при помощи `[]`. Пример: `Array('a')[0] == 'a'`

Требования:

- Хранить состояние `Array` в свойстве `self._data`, использовать `tuple`
- Наследоваться нужно и можно только от `object`
