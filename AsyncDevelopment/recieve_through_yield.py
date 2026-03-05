from collections import  deque
from types import coroutine

friends = deque(('rolf','jose','chrlie','jen','aana'))

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greetings = yield
        print(f'{greetings} {friend}')


async def greet(g):
    await g

    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)


greeter = greet(friend_upper())
greeter.send(None)
greeter.send("Hellow")
print("multitasking on going ====")
greeter.send("Hellow")
greeter.send("Hellow")
greeter.send("Hellow")
greeter.send("Hellow")
greeter.send("Hellow")