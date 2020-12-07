from functools import reduce


class Day7:
    def run_a(self, input_file):
        bags_dict = self.__read(input_file)
        bag_to_find = Bag(1, 'shiny', 'gold')

        found_bags = 0
        for contained_bags in bags_dict.values():
            result = any([self.__find_bag(bag, bag_to_find, bags_dict)
                          for bag in contained_bags])
            if result:
                found_bags += 1
        return found_bags

    def run_b(self, input_file):
        bags_dict = self.__read(input_file)
        start_bag = Bag(1, 'shiny', 'gold')

        found_bags = self.__count_bags(start_bag, bags_dict, 0)
        return found_bags

    def __find_bag(self, bag, bag_to_find, bags_dict):
        if bag.equals(bag_to_find):
            return True

        contained_bags = bags_dict[bag.key()]
        return any([self.__find_bag(bag, bag_to_find, bags_dict) for bag in contained_bags])

    def __count_bags(self, bag, bags_dict, count):
        contained_bags = bags_dict[bag.key()]

        return sum([bag.amount + (bag.amount * self.__count_bags(bag, bags_dict, count)) for bag in contained_bags])

    def __read(self, file_name):
        bags_dict = {}
        with open(file_name) as f:
            for line in f:
                bag_key, contained_bags = self.__read_line(line.rstrip())
                bags_dict[bag_key] = contained_bags
        return bags_dict

    def __read_line(self, line):
        index = 4
        words = line.split()

        shade, color = words[0], words[1]
        bag = Bag(1, shade, color)
        contained_bags = []
        while (index < len(words)):
            if words[index] != 'no':
                amount = int(words[index])
                shade = words[index + 1]
                color = words[index + 2]
                included_bag = Bag(amount, shade, color)
                contained_bags.append(included_bag)
            index += 4

        return bag.key(), contained_bags


class Bag:
    def __init__(self, amount, shade, color):
        self.amount = amount
        self.shade = shade
        self.color = color

    def equals(self, bag):
        return self.shade == bag.shade and self.color == bag.color

    def key(self):
        return self.shade + '-' + self.color

    def print(self):
        print('amount: ' + str(self.amount) + ', shade: ' +
              self.shade + ', color: ' + self.color)


if __name__ == '__main__':
    day = Day7()

    input_file = 'day7/7.txt'

    result_a = day.run_a(input_file)
    print(result_a)

    result_b = day.run_b(input_file)
    print(result_b)
