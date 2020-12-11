# Horror all over the place...

def run_a(input_file):
    seats = _read(input_file)
    rows, columns = _dimensions(seats)

    while True:
        empty_seats = _empty_seats(rows, columns)
        new_seats, changes = _round(seats, empty_seats, rows, columns, 'a')
        seats = new_seats
        if changes == 0:
            break

    return _occupied(new_seats)


def run_b(input_file):
    seats = _read(input_file)
    rows, columns = _dimensions(seats)

    while True:
        empty_seats = _empty_seats(rows, columns)
        new_seats, changes = _round(seats, empty_seats, rows, columns, 'b')
        seats = new_seats
        if changes == 0:
            break

    return _occupied(new_seats)


def _occupied(seats):
    occupied = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                occupied += 1
    return occupied


def _dimensions(seats):
    rows = len(seats)
    columns = len(seats[0])
    return rows, columns


def _empty_seats(rows, columns):
    return [[0 for i in range(columns)] for j in range(rows)]


def _round(seats, empty_seats, rows, columns, part):
    changes = 0
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            new_seat = seat
            if part == 'a':
                occupied_count = 4
                adjacent_seats = _adjacent_seats_a(
                    i, j, seats, rows, columns)
            else:
                occupied_count = 5
                adjacent_seats = _adjacent_seats_b(i, j, seats, rows, columns)
            if seat == 'L' and '#' not in adjacent_seats:
                new_seat = '#'
                changes += 1
            elif seat == '#' and adjacent_seats.count('#') >= occupied_count:
                new_seat = 'L'
                changes += 1
            empty_seats[i][j] = new_seat

    return empty_seats, changes


def _adjacent_seats_a(i, j, seats, rows, columns):
    adjacent_seats = []
    adjacents = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                 (0, 1), (1, -1), (1, 0), (1, 1)]

    for y, x in adjacents:
        if 0 <= i - y < rows and 0 <= j - x < columns:
            adjacent_seats.append(seats[i - y][j - x])

    return adjacent_seats


def _adjacent_seats_b(i, j, seats, rows, columns):
    on_row = _find_on_row(i, j, seats, rows, columns)
    on_column = _find_on_column(i, j, seats, rows, columns)
    on_diagonal = _find_on_diagonal(i, j, seats, rows, columns)
    adjacent_seats = on_row + on_column + on_diagonal
    return adjacent_seats


def _find_on_row(i, j, seats, rows, columns):
    left = '.'
    right = '.'
    x = 0
    while left == '.' and j - x > 0:
        x += 1
        left = seats[i][j - x]
    x = 0
    while right == '.' and j - x < columns - 1:
        x -= 1
        right = seats[i][j - x]

    result = []
    if left != '.':
        result.append(left)
    if right != '.':
        result.append(right)

    return result


def _find_on_column(i, j, seats, rows, columns):
    up = '.'
    down = '.'
    y = 0
    while up == '.' and i - y > 0:
        y += 1
        up = seats[i - y][j]
    y = 0
    while down == '.' and i - y < rows - 1:
        y -= 1
        down = seats[i - y][j]

    result = []
    if up != '.':
        result.append(up)
    if down != '.':
        result.append(down)

    return result


def _find_on_diagonal(i, j, seats, rows, columns):
    leftup = '.'
    rightup = '.'
    leftdown = '.'
    rightdown = '.'
    y = 0
    x = 0
    while leftup == '.' and i - y > 0 and j - x > 0:
        y += 1
        x += 1
        leftup = seats[i - y][j - x]
    y = 0
    x = 0
    while rightup == '.' and i - y > 0 and j - x < columns - 1:
        y += 1
        x -= 1
        rightup = seats[i - y][j - x]
    y = 0
    x = 0
    while leftdown == '.' and i - y < rows - 1 and j - x > 0:
        y -= 1
        x += 1
        leftdown = seats[i - y][j - x]
    y = 0
    x = 0
    while rightdown == '.' and i - y < rows - 1 and j - x < columns - 1:
        y -= 1
        x -= 1
        rightdown = seats[i - y][j - x]

    result = []
    if leftup != '.':
        result.append(leftup)
    if rightup != '.':
        result.append(rightup)
    if leftdown != '.':
        result.append(leftdown)
    if rightdown != '.':
        result.append(rightdown)

    return result


def _read(file_name):
    with open(file_name) as f:
        input = [list(line.rstrip()) for line in f]

    return input


def run():
    input_file = 'day11/11.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    run()
