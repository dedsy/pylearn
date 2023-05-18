## Теория

### Материалы по Python

- Документация `tuple`: https://docs.python.org/3/library/stdtypes.html#typesseq-tuple
- Документация `list`: https://docs.python.org/3/tutorial/datastructures.html
- Документация `dict`: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- `tuple` vs `list`: http://stackoverflow.com/questions/1708510/python-list-vs-tuple-when-to-use-each http://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples http://nedbatchelder.com/blog/201608/lists_vs_tuples.html
- `dict`: https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html
- Что такое функция? https://www.tutorialspoint.com/python/python_functions.htm
- Что значит - вызвать функцию? https://stackoverflow.com/questions/19130958/what-does-it-mean-to-call-a-function-in-python
- Что такое `*args` и `**kwargs`: https://lancelote.gitbooks.io/intermediate-python/content/book/args_and_kwargs.html

### Материалы для продвинутых

- Что такое хеш-таблицы? https://ru.wikipedia.org/wiki/%D0%A5%D0%B5%D1%88-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0
- Какие бывают списки? https://en.wikipedia.org/wiki/Linked_list#Linked_lists_vs._dynamic_arrays
- Как устроен список внутри? https://www.quora.com/How-are-Python-lists-implemented-internally
- Что такое `Sequence`: https://docs.python.org/3/library/stdtypes.html#typesseq
- Что такое `Iterable`: https://docs.python.org/3/glossary.html#term-iterable
- Сложность операций: https://wiki.python.org/moin/TimeComplexity
- Modern dictionaries (from Python Core developer): https://www.youtube.com/watch?v=p33CVV29OG8


## Практика

Требования:
- Правила игры в пятнашки: https://ru.wikipedia.org/wiki/%D0%98%D0%B3%D1%80%D0%B0_%D0%B2_15
- Поле состоит из клеток от 1 до 15 и пустой клетки
- Управление ведется кнопками "wasd", двигается пустая клетка
- В начале игры поле перемешено в случайном порядке
- Пользователь не должен совершать непозволительные шаги. Например, из-за ограничений рамки поля. Ему должно показываться сообщение о том, что он пытается совершить непозволительный ход
- Пользователю должно быть видно поле. Оно представляет собой матрицу 4 на 4. Пустую клетку обозначаем как x. При каждом действии пользователя поле рисуется еще раз - ниже в консоли
- Игра заканчивается, когда все клетки стоят по-порядку, а пустая клетка - последняя. В конце игры пользователю показывается, сколько ходов он совершил
- Выход из игры происходит при помощи `ctrl + c`

Технические требования:
- Игра должна соответствовать интерфейсу из файла game.py. Под "соответствовать интерфейсу" следует понимать: программа может иметь только те константы и функции, что уже опеределенны, сам файл должен называться: `game.py`
- Внутри реализуемых функций может происходить любая логика
- Поле должно быть реализовано как плоский список

Задача для продвинутых, необязательно:
- Обратите внимание, что не любое поле оставляет возможность закончить игру, необходимо придумать корректный алгоритм генерации взамен простого перемешивания
- Можете попробовать запустить тесты, которые приложены для проверки при помощи `pytest`
