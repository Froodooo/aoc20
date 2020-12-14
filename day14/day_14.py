import re
import itertools


def run_a(input_file):
    options = {'part': 'a'}
    return _run(input_file, options)


def run_b(input_file):
    options = {'part': 'b'}
    return _run(input_file, options)


def _run(input_file, options):
    program = _read(input_file)
    mask = '{:036b}'.format(0)
    memory = {}

    for line in program:
        mask, memory = _execute_line(line, mask, memory, options)

    return _get_memory_sum(memory)


def _execute_line(line, mask, memory, options):
    if line.startswith('mask'):
        mask = _get_mask(line)
    else:
        position, value = _get_memory(line, mask)
        if options['part'] == 'a':
            memory = _set_memory(position, value, mask, memory)
        elif options['part'] == 'b':
            memory = _set_memory_v2(position, value, mask, memory)

    return mask, memory


def _get_mask(line):
    return line.lstrip('mask = ')


def _get_memory(line, mask):
    position, value = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
    position, value = int(position), int(value)
    value = '{:036b}'.format(value)

    return position, value


def _set_memory(position, value, mask, memory):
    memory[position] = ''.join(
        [v if m == 'X' else m for v, m in zip(value, mask)])

    return memory


def _set_memory_v2(position, value, mask, memory):
    position = '{:036b}'.format(position)
    result = [m if m != '0' else v for v, m in zip(position, mask)]
    positions_of_X = [index for index, x in enumerate(result) if x == 'X']
    number_of_X = len(positions_of_X)
    size = pow(2, number_of_X)

    for i in range(size):
        bits_string = '{:0{size}b}'.format(i, size=number_of_X)
        bits = list(bits_string)
        address = result
        for p, b in zip(positions_of_X, bits):
            address[p] = b
        address_string = ''.join([str(x) for x in address])
        address_number = int(address_string, 2)
        memory[address_number] = value

    return memory


def _get_memory_sum(memory):
    return sum([int(x, 2) for x in memory.values()])


def _read(file_name):
    input = {}
    with open(file_name) as f:
        input = f.readlines()

    return input


def solve():
    input_file = 'day14/14.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
