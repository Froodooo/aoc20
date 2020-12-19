import re


def run_a(input_file):
    options = {'part': 'a'}
    rules, lines = _read(input_file)
    resolved = _resolve('0', rules, options)
    resolved_regex = f'^{resolved}$'

    result = 0
    for line in lines:
        if re.match(resolved_regex, line):
            result += 1

    return result


def run_b(input_file):
    options = {'part': 'b'}
    rules, lines = _read(input_file)
    resolved = _resolve('0', rules, options)
    resolved_regex = f'^{resolved}$'

    result = 0
    for line in lines:
        if re.match(resolved_regex, line):
            result += 1

    return result


def _resolve(rule_number, rules, options):
    if options['part'] == 'b':
        if rule_number == '8':
            return f'({_resolve("42", rules, options)})+'
        elif rule_number == '11':
            return '|'.join((_resolve_char('42', rules, options) * n) +
                            (_resolve_char('31', rules, options) * n) for n in range(1, 20))

    rule = rules[rule_number]
    return ''.join(_resolve_char(char, rules, options) for char in rule)


def _resolve_char(char, rules, options):
    if char in 'ab|':
        return char
    else:
        return f'({_resolve(char, rules, options)})'


def _read(file_name):
    with open(file_name) as f:
        rules, input = f.read().split('\n\n')
        rules = _read_rules(rules)
        input = _read_input(input)

    return rules, input


def _read_rules(rules):
    rules_dict = {}
    for rule in rules.split('\n'):
        rule_number, rule_content = rule.split(': ')
        rules_dict[rule_number] = rule_content.replace('"', '').split()

    return rules_dict


def _read_input(input):
    return [line for line in input.split('\n')]


def solve():
    input_file = 'day19/19.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
