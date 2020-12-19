def run_a(input_file):
    _ = _read(input_file)
    return 0


def _read(file_name):
    with open(file_name) as f:
        input = [line for line in f]

    return input


def solve():
    input_file = 'day20/20.txt'

    result_a = run_a(input_file)
    print(result_a)

    # result_b = run_b(input_file)
    # print(result_b)


if __name__ == '__main__':
    solve()
