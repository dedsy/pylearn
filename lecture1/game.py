questions = {
    'Какая версия языка сейчас актуальна?': 'Python3',
    'Какая кодировка используется в строках?': 'UTF8',
    'Сколько значений есть у bool?': 2,
    'Какой тип данных для целых чисел?': 'int',
    'Какой тип данных для строк?': 'str',
    'Какой тип данных для дробных чисел?': 'float',
    'Специальный тип данных для обозначения "ничего"?': 'None',
    'Цикл с предусловием?': 'while',
    '"Перебирающий" итератор?': 'for',
    'Набор стилевых рекомендаций по написанию кода Python?': 'pep8',
}


def quiz(q_dict):
    right_answers = 0
    for item in q_dict.items():
        users_input = input(item[0] + "\n")
        if str(users_input.upper()) == str(item[1]).upper():
            print('Ответ "{0}" - верен'.format(users_input))
            right_answers += 1
        else:
            print('Неверный ответ.')
    return 'Вы ответили правильно на {0} вопросов'.format(right_answers)


print(quiz(questions))
