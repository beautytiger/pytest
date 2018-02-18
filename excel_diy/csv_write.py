import random
from time import time

LINES = 10**6
before = time()
with open('random.csv', 'w') as f:
    for i in range(LINES):
        data = []
        for j in range(5):
            data.append(random.randint(1, 100))
        string = ','.join(map(str, data))
        string += '\n'
        f.write(string)
after = time()
print(LINES, ' ', after-before)
