def run_a(input_file, preamble):
    input = _read(input_file)
    weakness = _find_weakness(input, preamble)

    return weakness


def run_b(input_file, preamble):
    input = _read(input_file)
    weakness = _find_weakness(input, preamble)
    contiguous_set = _find_contiguous_set(input, weakness)

    return min(contiguous_set) + max(contiguous_set)


def _find_weakness(input, preamble):
    for index, number in enumerate(input[preamble:]):
        has_weakness = _has_weakness(number, input[index:(preamble + index)])
        if has_weakness:
            return number

    return 0


def _has_weakness(number, input):
    for x in input:
        for y in input:
            if x != y and x + y == number:
                return False

    return True


def _find_contiguous_set(input, weakness):
    total = 0
    for index, _ in enumerate(input):
        count = 0
        total = 0
        while(total < weakness):
            total += input[index + count]
            count += 1
            if total == weakness:
                return input[index:(index + count)]


def _read(file_name):
    with open(file_name) as f:
        input = [int(line.rstrip()) for line in f]

    return input


def run():
    input_file = 'day9/9.txt'

    preamble = 25

    result_a = run_a(input_file, preamble)
    print(result_a)

    result_b = run_b(input_file, preamble)
    print(result_b)


if __name__ == '__main__':
    run()
