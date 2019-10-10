# coding: utf-8

import logging, threading

from queue import Queue

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

shared_queue = Queue()
queue_condition = threading.Condition()

def divisibility_task(condition, q):
    with condition:
        while shared_queue.empty():
            logger.info("[%s] - waiting for element in queue..." % threading.current_thread().name)
            condition.wait()
        else:
            value = shared_queue.get()
            print('{} divisible by {} is {}'.format(value, q, not bool(value%q)))
        shared_queue.task_done()

def queue_task(condition):
    logging.debug("Starting queue_task...")
    with condition:
        for item in range(30):
            shared_queue.put(item)
        logging.debug("Notifying fibonacci_task threads that the queue is ready to consume...")
        condition.notifyAll()

threads = [threading.Thread(daemon=True, target=divisibility_task, args=(queue_condition,q,)) for q in [3, 5]]

[thread.start() for thread in threads]

prod = threading.Thread(name="queue_task_thread", daemon=True, target=queue_task, args=(queue_condition,))
prod.start()

[thread.join() for thread in threads]

