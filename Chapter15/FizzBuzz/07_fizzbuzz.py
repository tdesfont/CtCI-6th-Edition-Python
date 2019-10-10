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
input_list = [3, 5, 15]

def check_divis_task(condition, value):
    with condition:
        while shared_queue.empty():
            logger.info("[%s] - waiting for element in queue..." % threading.current_thread().name)
            condition.wait()
        else:
            divisor = shared_queue.get()
            if not value % divisor:
                print('Value {} is divisible by {}'.format(value, divisor))
            else:
                print('Value {} is not divisible by {}'.format(value, divisor))
        shared_queue.task_done()
        logger.debug("[%s] check div of value [%d] with divisor [%d]" % (threading.current_thread().name, value, divisor))

def queue_task(condition):
    logging.debug("Starting queue_task...")
    with condition:
        for item in input_list:
            shared_queue.put(item)
        logging.debug("Notifying threads that the queue is ready to consume...")
        condition.notifyAll()

for value in range(20):
    threads = [threading.Thread(daemon=True, target=check_divis_task, args=(queue_condition,value,)) for i in range(3)]
    [thread.start() for thread in threads]
    prod = threading.Thread(name="queue_task_thread", daemon=True, target=queue_task, args=(queue_condition,))
    prod.start()
    [thread.join() for thread in threads]