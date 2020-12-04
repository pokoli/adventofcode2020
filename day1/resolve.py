import os
from itertools import combinations

expenses = []
with open(os.path.join('.', 'input.txt')) as f:
    for line in f.readlines():
        expenses.append(int(line))

for a, b in combinations(expenses, 2):
    if a + b == 2020:
        print('Found two numbers ({a}, {b}) that sum 2020'.format(**locals()))
        print('Its multiplication is {mul}'.format(mul=a * b))
        break

for a, b, c in combinations(expenses, 3):
    if a + b + c == 2020:
        print('Found three numbers ({a}, {b}, {c}) that sum 2020'.format(
                **locals()))
        print('Its multiplication is {mul}'.format(mul=a * b * c))
        break
