import random


row = "+-----+-----+-----+-----+"


def board(seq):
    print(row)
    for i in range(0, 16):
        if seq[i] < 10:
            if seq[i] == 0:
                print('| ' + 'X' + ' ', end='  ')
            else:
                print('| ' + str(seq[i]) + ' ', end='  ')
        else:
            num = str(seq[i])
            print('| '+num[0]+' '+num[1]+' ', end='')
        if i == 3 or i == 7 or i == 11:
            print('|')
            print(row)
    print('|')
    print(row)


def check_input():
    while True:
        user_input = input('Введите направление движения x с помощью WASD: ')
        if user_input.upper() not in 'WASD':
            print('Введите направление с помощью WASD.')
        elif len(user_input) > 1:
            print('Направление должно содержать только 1 символ.')
        else:
            return str(user_input.upper())


def random_list():
    line = list(range(16))
    random.shuffle(line)
    return line


def find_x():
    x_index = [(index, i.index(0)) for index, i in enumerate(matrix) if 0 in i]
    return x_index


def possible_move(seq):
    pos_turns = {}
    step_row = find_x()[0][0]
    step_coll = find_x()[0][1]
    if step_row == 0:
        if step_coll != 0 and step_coll != 3:
            pos_turns.update({'A': seq[step_row][step_coll - 1], 'S': seq[step_row + 1][step_coll], 'D': seq[step_row][step_coll + 1]})
        elif step_coll == 0:
            pos_turns.update({'S': seq[step_row + 1][step_coll], 'D': seq[step_row][step_coll + 1]})
        else:
            pos_turns.update({'A': seq[step_row][step_coll - 1], 'S': seq[step_row + 1][step_coll]})
    elif step_row == 3:
        if step_coll != 0 and step_coll != 3:
            pos_turns.update({'W': seq[step_row - 1][step_coll], 'A': seq[step_row][step_coll - 1], 'D': seq[step_row][step_coll + 1]})
        elif step_coll == 0:
            pos_turns.update({'W': seq[step_row - 1][step_coll], 'D': seq[step_row][step_coll + 1]})
        else:
            pos_turns.update({'W': seq[step_row - 1][step_coll], 'A': seq[step_row][step_coll - 1]})
    else:
        if step_coll != 0 and step_coll != 3:
            pos_turns.update({'W': seq[step_row - 1][step_coll], 'A': seq[step_row][step_coll - 1], 'S': seq[step_row + 1][step_coll], 'D': seq[step_row][step_coll + 1]})
        elif step_coll == 0:
            pos_turns.update({'W': seq[step_row - 1][step_coll], 'S': seq[step_row + 1][step_coll], 'D': seq[step_row][step_coll + 1]})
        else:
            pos_turns.update({'W': seq[step_row - 1][step_coll], 'S': seq[step_row + 1][step_coll], 'A': seq[step_row][step_coll - 1]})

    return pos_turns


new_seq = random_list()
victory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
turns = 0

# print(possible_move(matrix))
board(new_seq)

while True:
    matrix = [new_seq[0:4], new_seq[4:8], new_seq[8:12], new_seq[12:16]]
    moves = possible_move(matrix)
    turn_dir = check_input()
    if turn_dir in moves.keys():
        zero_index = new_seq.index(0)
        target = moves[turn_dir]
        target_index = new_seq.index(target)
        new_seq[zero_index] = target
        new_seq[target_index] = 0
        turns += 1
        board(new_seq)
    else:
        print('Такой ход невозможен!')

    if new_seq == victory:
        print('Победа!')
        print(f'Колличество ходов для победы: {turns} ')
        break
