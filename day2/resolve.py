import os
from collections import Counter

passwords = []
with open(os.path.join('.', 'input.txt')) as f:
    for line in f.readlines():
        passwords.append(line.split(': '))


def is_valid(line):
    policy, password = line
    counts, char = policy.split(' ')
    min_, max_ = map(int, counts.split('-'))
    char_count = Counter(password).get(char, 0)
    return min_ <= char_count <= max_


valid = list(filter(is_valid, passwords))
print("Found {} valid passwords".format(len(valid)))


def is_valid_part2(line):
    policy, password = line
    counts, char = policy.split(' ')
    min_, max_ = map(int, counts.split('-'))
    first = password[min_ - 1] == char
    second = password[max_ - 1] == char
    return (first and not second) or (second and not first)


valid = list(filter(is_valid_part2, passwords))
print("Found {} valid passwords following new interpretation".format(
        len(valid)))
