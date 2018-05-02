from time import time
import random
import string

for length in range(1, 10):
    container = set()
    before = time()
    while True:
        flow = [random.choice(string.digits+string.ascii_lowercase) for i in range(length)]
        flow = ''.join(flow)
        # print(flow)
        if flow in container:
            after = time()
            duration = after - before
            total = len(container)
            print(length, " time: ", duration, " count: ", total)
            break
        container.add(flow)

"""
1  time:  2.384185791015625e-05  count:  9
2  time:  5.984306335449219e-05  count:  20
3  time:  0.0014045238494873047  count:  358
4  time:  0.012720584869384766  count:  2235
5  time:  0.08954334259033203  count:  16870
6  time:  0.16925644874572754  count:  28885
7  time:  1.832322120666504  count:  282789
8  time:  2.173828363418579  count:  298728
9  time:  177.3634569644928  count:  20991732
"""
