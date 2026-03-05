import time
from threading import Thread

def ask_user():
    start = time.time()
    user_input = input("Please enter your name: ")
    greet = f"Hello {user_input}!"
    print(greet)
    print(f'ask user {time.time()-start} seconds')

def complex_calculation():
    start = time.time()
    print("Starting calculating /... ")
    [x**2 for x in range(20000000)]
    print(f'complex_calculation {time.time() - start} seconds')

start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start} ')

#
# thread1 = Thread(target=complex_calculation)
# thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()
thread2.start()

# Blocking operation
thread1.join() # this tells process that wait for thread 1 to run
thread2.join() # this tells process that wait for thread 2 to run

print(f'Multi thread total time: {time.time() - start} ')