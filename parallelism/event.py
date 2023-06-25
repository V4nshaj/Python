import threading
import time
item = None
# A semaphore to indicate that an item is available
available = threading.Semaphore(0)
# An event to indicate that processing is complete
completed = threading.Event()
# A worker thread
def worker():
    while True:
        available.acquire()
        print ("worker: processing", item)
        time.sleep(5)
        print ("worker: done")
        completed.set()
# A producer thread
def producer():
    global item
    for x in range(5):
        completed.clear()       # Clear the event
        item = x                # Set the item
        print ("producer: produced an item")
        available.release()     # Signal on the semaphore
        completed.wait()
        print ("producer: item was processed")
t1 = threading.Thread(target=producer)
t1.start()
t2 = threading.Thread(target=worker)
t2.setDaemon(True)
t2.start()
