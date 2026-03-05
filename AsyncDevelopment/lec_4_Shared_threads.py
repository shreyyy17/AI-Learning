#Atomic operation : you can not intrupt in the middle
# you first need to wait for finish it

#to use multiple threads to call the same function you needed the queuing system


import time
import random
import queue

from threading import Thread

counter = 0



job_queue = queue.Queue() # things to be printed out
counter_queue = queue.Queue() #amounts by which to increase the counter

def increment_manager():
    global counter
    while True:
        increment = counter_queue.get() # this waits until an item is available This locks the queue
        time.sleep(random.random())
        old_counter = counter
        time.sleep(random.random())

        counter = old_counter + increment
        time.sleep(random.random())

        job_queue.put((f'New counter value is {counter}','-----------------'))
        time.sleep(random.random())

        counter_queue.task_done() # unlocks the queue

    print("=============")


Thread(target=increment_manager, daemon=True).start()

def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
            time.sleep(random.random())

        job_queue.task_done()


Thread(target=printer_manager, daemon=True).start()


def increament_counter():
    counter_queue.put(1)

worker_threads = [Thread(target=increament_counter) for thread in range(10)]

for thread in worker_threads:
    time.sleep(random.random())
    thread.start()

for thread in worker_threads:
    thread.join()

counter_queue.join()
job_queue.join()




# for x in range(10):
#     t =Thread(target=increment_val)
#     time.sleep(random.random())
#     t.start()
#     # increment_val()
