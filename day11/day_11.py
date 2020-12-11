from copy import deepcopy
from time import time

ADJACENTS = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
             (0, 1), (1, -1), (1, 0), (1, 1)]

EMPTY_CHAIR = 'L'
OCCUPIED_CHAIR = '#'
FLOOR = '.'


def run_a(input_file):
    options = {'part': 'a', 'occupied_count': 4}
    return _run(input_file, options)


def run_b(input_file):
    options = {'part': 'b', 'occupied_count': 5}
    return _run(input_file, options)


def _run(input_file, options):
    seats = _read(input_file)
    changed = True

    while changed:
        seats, changed = _round(seats, options)

    return _occupied(seats)


def _round(seats, options):
    rows, cols = len(seats), len(seats[0])
    seats_copy = deepcopy(seats)
    changed = False

    for row in range(rows):
        for col in range(cols):
            adjacent_seats = _adjacent_seats(row, col, seats, options)
            new_seat = seats[row][col]
            if new_seat == EMPTY_CHAIR and OCCUPIED_CHAIR not in adjacent_seats:
                new_seat = OCCUPIED_CHAIR
                changed = True
            elif new_seat == OCCUPIED_CHAIR and adjacent_seats.count(OCCUPIED_CHAIR) >= options['occupied_count']:
                new_seat = EMPTY_CHAIR
                changed = True

            seats_copy[row][col] = new_seat

    return seats_copy, changed


def _adjacent_seats(row, col, seats, options):
    if options['part'] == 'a':
        adjacent_seats = _direct_ajacent_seats(
            row, col, seats)
    elif options['part'] == 'b':
        adjacent_seats = _indirect_adjacent_seats(
            row, col, seats)
    return adjacent_seats


def _direct_ajacent_seats(row, col, seats):
    adjacent_seats = []
    rows, cols = len(seats), len(seats[0])

    for adjacent_row, adjacent_col in ADJACENTS:
        if 0 <= row - adjacent_row < rows and 0 <= col - adjacent_col < cols:
            adjacent_seats.append(
                seats[row - adjacent_row][col - adjacent_col])

    return adjacent_seats


def _indirect_adjacent_seats(row, col, seats):
    adjacent_seats = []
    rows, cols = len(seats), len(seats[0])

    for adjacent_row, adjacent_col in ADJACENTS:
        row_delta = row + adjacent_col
        col_delta = col + adjacent_row

        while _seat_is_floor(row_delta, col_delta, seats):
            row_delta += adjacent_col
            col_delta += adjacent_row

        if 0 <= row_delta < rows and 0 <= col_delta < cols:
            adjacent_seats.append(
                seats[row_delta][col_delta])

    return adjacent_seats


def _seat_is_floor(row, col, seats):
    rows, cols = len(seats), len(seats[0])

    return 0 <= row < rows and 0 <= col < cols and seats[row][col] == FLOOR


def _occupied(seats):
    occupied = 0
    for row in seats:
        for seat in row:
            if seat == OCCUPIED_CHAIR:
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
