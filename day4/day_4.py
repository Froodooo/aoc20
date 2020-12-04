import re


class Day4:
    def run_a(self, input_file):
        input = self.__read(input_file)
        required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        validated_input = [self.__is_valid_a(
            line, required.copy()) for line in input]
        valid_passports = validated_input.count(True)
        return(valid_passports)

    def run_b(self, input_file):
        input = self.__read(input_file)
        required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        validated_input = [self.__is_valid_b(
            line, required.copy()) for line in input]
        valid_passports = validated_input.count(True)
        return(valid_passports)

    def __is_valid_a(self, line, required):
        for (field, _) in line:
            if (field == 'cid'):
                continue
            required.remove(field)
        return len(required) == 0

    def __is_valid_b(self, line, required):
        for (field, value) in line:
            if (field == 'cid'):
                continue
            is_valid_field = self.__is_valid_field(field, value)
            if (is_valid_field):
                required.remove(field)
        return len(required) == 0

    def __is_valid_field(self, field, value):
        if (field == 'byr'):
            return int(value) in range(1920, 2003)
        elif (field == 'iyr'):
            return int(value) in range(2010, 2021)
        elif (field == 'eyr'):
            return int(value) in range(2020, 2031)
        elif (field == 'hgt'):
            hgt_regex = r'(\d+)(cm|in)'
            if not (re.match(hgt_regex, value)):
                return False
            [(height, unit)] = re.findall(hgt_regex, value)
            if (unit == 'cm'):
                return int(height) in range(150, 194)
            elif (unit == 'in'):
                return int(height) in range(59, 77)
            else:
                return False
        elif (field == 'hcl'):
            return re.match('#([0-9a-f]{6})', value)
        elif (field == 'ecl'):
            return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif (field == 'pid'):
            return re.match('^0*[0-9]{9}$', value)
        else:
            False

    def __read(self, file_name):
        with open(file_name) as f:
            input = f.read().rstrip().split('\n\n')
            input = [re.split('\n| ', line) for line in input]
            input = [self.__split(line) for line in input]
        return input

    def __split(self, line):
        return [tuple(field.split(':')) for field in line]


if __name__ == '__main__':
    day = Day4()

    input_file = 'day4/4.txt'

    result_a = day.run_a(input_file)
    print(result_a)

    result_b = day.run_b(input_file)
    print(result_b)
