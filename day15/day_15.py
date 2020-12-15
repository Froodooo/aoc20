class Game:
    def __init__(self, numbers):
        self.previous = numbers[-1]
        self.state = {}
        self.turns = len(numbers)

        for turn, number in enumerate(numbers[:-1]):
            self.state[number] = [turn + 1]

    def play(self):
        self.turns += 1
        
        if self.previous in self.state:
            numbers = self.state[self.previous]
            numbers.append(self.turns - 1)
            self.state[self.previous] = numbers
            new_number = numbers[-1] - numbers[-2]
            self.previous = new_number
        else:
            self.state[self.previous] = [self.turns - 1]
            new_number = 0
            self.previous = new_number

    def get_turns(self):
        return self.turns

    def get_previous(self):
        return self.previous


def run_a(input_file):
    input = _read(input_file)
    game = Game(input)
    while game.get_turns() < 2020:
        game.play()

    return game.get_previous()


def run_b(input_file):
    input = _read(input_file)
    game = Game(input)
    while game.get_turns() < 30000000:
        game.play()

    return game.get_previous()


def _read(file_name):
    input = {}
    with open(file_name) as f:
        input = [int(number) for number in f.readline().split(',')]

    return input


def solve():
    input_file = 'day15/15.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
