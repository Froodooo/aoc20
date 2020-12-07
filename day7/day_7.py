from functools import reduce


class Bag:
    def __init__(self, amount, shade, color):
        self.amount = amount
        self.shade = shade
        self.color = color

    def equals(self, bag):
        return self.shade == bag.shade and self.color == bag.color

    def key(self):
        return self.shade + '-' + self.color


def run_a(input_file):
    bags = _read(input_file)
    bag_to_find = Bag(1, 'shiny', 'gold')

    found_bags = 0
    for contained_bags in bags.values():
        if any([_find_bag(bag, bag_to_find, bags) for bag in contained_bags]):
            found_bags += 1

    return found_bags


def run_b(input_file):
    bags = _read(input_file)
    start_bag = Bag(1, 'shiny', 'gold')

    return _count_bags(start_bag, bags, 0)


def _find_bag(bag, bag_to_find, bags):
    if bag.equals(bag_to_find):
        return True

    contained_bags = bags[bag.key()]

    return any([_find_bag(bag, bag_to_find, bags) for bag in contained_bags])


def _count_bags(bag, bags, count):
    contained_bags = bags[bag.key()]

    return sum([bag.amount + (bag.amount * _count_bags(bag, bags, count)) for bag in contained_bags])


def _read(file_name):
    bags = {}
    with open(file_name) as f:
        for line in f:
            bag_key, contained_bags = _read_line(line.rstrip())
            bags[bag_key] = contained_bags

    return bags


def _read_line(line):
    words = line.split()

    shade, color = words[0], words[1]
    bag = Bag(1, shade, color)

    contained_bags = []
    index = 4

    while (index < len(words)):
        if words[index] != 'no':
            amount = int(words[index])
            shade = words[index + 1]
            color = words[index + 2]
            contained_bags.append(Bag(amount, shade, color))
        index += 4

    return bag.key(), contained_bags


def run():
    input_file = 'day7/7.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    run()
