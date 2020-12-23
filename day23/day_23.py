from operator import mul
from functools import reduce


def run_a(input_file, moves):
    numbers = _read(input_file)
    options = {'next': 3}
    numbers = _play_game(numbers, moves, options)
    collected_numbers = _collect_numbers(numbers, 1)

    return ''.join("{0}".format(n) for n in collected_numbers)


def run_b(input_file, moves):
    numbers = _read(input_file)
    numbers = _pad_until(numbers, 1000000)
    options = {'next': 3}
    numbers = _play_game(numbers, moves, options)
    collected_numbers = _collect_next_numbers_after(numbers, 1, 2)

    return reduce(mul, collected_numbers)


def _pad_until(numbers, until):
    return numbers + [i for i in range(max(numbers) + 1, until + 1)]


def _collect_next_numbers_after(numbers, after, amount):
    collected_numbers = []
    after_index = numbers.index(after)
    for i in range(1, amount + 1):
        collected_numbers.append(numbers[(after_index + i) % len(numbers)])

    return collected_numbers


def _collect_numbers(numbers, from_cup):
    from_cup_index = numbers.index(from_cup)
    collected_numbers = []

    for i in range(1, len(numbers)):
        collected_numbers.append(numbers[(from_cup_index + i) % len(numbers)])

    return collected_numbers


def _play_game(numbers, moves, options):
    current_cup = numbers[0]
    next = options['next']

    for move in range(moves):
        # print(f'-- move {move + 1} --')

        numbers = _adjust_spacing(numbers, current_cup, move)
        current_cup_index = numbers.index(current_cup)
        next_cup = numbers[(current_cup_index + next + 1) % len(numbers)]

        # print('cups:', numbers)
        # print('current:', current_cup)

        picked_up = []
        for i in range(1, next + 1):
            index = (current_cup_index + i) % len(numbers)
            picked_up.append(numbers[index])
        for cup in picked_up:
            numbers.remove(cup)
        # print('pick up:', picked_up)

        destination_cup = current_cup
        while destination_cup in picked_up or destination_cup == current_cup:
            destination_cup -= 1
            if destination_cup < min(numbers):
                destination_cup = max(numbers)
                break
        # print('destination:', destination_cup)
        destination_cup_index = numbers.index(destination_cup)

        for i in range(1, next + 1):
            numbers.insert(destination_cup_index + i, picked_up[i - 1])

        current_cup = next_cup

    return numbers


def _adjust_spacing(numbers, current_cup, move):
    collected_numbers = _collect_numbers(numbers, current_cup)
    collected_numbers = collected_numbers[-(move % len(
        numbers)):] + collected_numbers[:-(move % len(numbers))]
    collected_numbers.insert((move % len(numbers)), current_cup)
    
    return collected_numbers


def _read(file_name):
    with open(file_name) as f:
        input = [int(number) for number in f.readline()]

    return input


def solve():
    input_file = 'day23/23.txt'

    result_a = run_a(input_file, 100)
    print(result_a)

    # result_b = run_b(input_file)
    # print(result_b)


if __name__ == '__main__':
    solve()
