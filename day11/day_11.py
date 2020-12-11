from copy import deepcopy

ADJACENTS = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
             (0, 1), (1, -1), (1, 0), (1, 1)]


def run_a(input_file):
    options = {'part': 'a', 'occupied_count': 4}
    return _run(input_file, options)


def run_b(input_file):
    options = {'part': 'b', 'occupied_count': 5}
    return _run(input_file, options)


def _run(input_file, options):
    seats = _read(input_file)
    dimensions = _dimensions(seats)

    while True:
        seats, changed = _round(seats, dimensions, options)
        if not changed:
            break

    return _occupied(seats)


def _round(seats, dimensions, options):
    empty_seats = deepcopy(seats)
    changed = False

    for row_index, row in enumerate(seats):
        for column_index, seat in enumerate(row):
            new_seat = seat
            adjacent_seats = _adjacent_seats(
                row_index, column_index, seats, dimensions, options)
            if seat == 'L' and '#' not in adjacent_seats:
                new_seat = '#'
                changed = True
            elif seat == '#' and adjacent_seats.count('#') >= options['occupied_count']:
                new_seat = 'L'
                changed = True

            empty_seats[row_index][column_index] = new_seat

    return empty_seats, changed


def _adjacent_seats(row_index, column_index, seats, dimensions, options):
    if options['part'] == 'a':
        adjacent_seats = _direct_ajacent_seats(
            row_index, column_index, seats, dimensions)
    elif options['part'] == 'b':
        adjacent_seats = _indirect_adjacent_seats(
            row_index, column_index, seats, dimensions)
    return adjacent_seats


def _direct_ajacent_seats(row_index, column_index, seats, dimensions):
    adjacent_seats = []
    rows, columns = dimensions

    for y, x in ADJACENTS:
        if 0 <= row_index - y < rows and 0 <= column_index - x < columns:
            adjacent_seats.append(seats[row_index - y][column_index - x])

    return adjacent_seats


def _indirect_adjacent_seats(row_index, column_index, seats, dimensions):
    adjacent_seats = []
    rows, columns = dimensions

    for y, x in ADJACENTS:
        row_index_delta = row_index + x
        column_index_delta = column_index + y

        while _seat_is_floor(row_index_delta, column_index_delta, seats, dimensions):
            row_index_delta += x
            column_index_delta += y

        if 0 <= row_index_delta < rows and 0 <= column_index_delta < columns:
            adjacent_seats.append(
                seats[row_index_delta][column_index_delta])

    return adjacent_seats


def _seat_is_floor(row, column, seats, dimensions):
    rows, columns = dimensions

    return 0 <= row < rows and 0 <= column < columns and seats[row][column] == '.'


def _dimensions(seats):
    rows = len(seats)
    columns = len(seats[0])

    return (rows, columns)


def _occupied(seats):
    occupied = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                occupied += 1

    return occupied


def _read(file_name):
    with open(file_name) as f:
        input = [list(line.rstrip()) for line in f]

    return input


def solve():
    input_file = 'day11/11.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
