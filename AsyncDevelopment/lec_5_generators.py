def count_down(n):
    while n > 0:
        yield n
        n -= 1

# c1 = count_down(10)
# c2 = count_down(20)
#
# print(next(c1))
# print(next(c2))
#
# print(next(c1))
# print(next(c2))

tasks = [count_down(10), count_down(20), count_down(30)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task completed')