# A queue where you can add or remove data from both
# sides us called in python a "deque" or "double-ended queue"
# else it is called as queue




"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""


## TimeZones ===================
from datetime import datetime, timezone, timedelta

# print(datetime.now(timezone.utc))


today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

# print(today.strftime("%d-%m-%Y %H:%M:%S"))
# print(tomorrow.strftime("%d-%m-%Y %H:%M:%S"))




import time

def power(limit):
    return [x**2 for x in range(limit)]

def measure_time(func):
    start = time.time()
    func()
    end = time.time()
    # print(end - start)


measure_time(lambda: power(5000000))


import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))
