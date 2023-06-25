import threading,time
items=[]
items_cv = threading.Condition()
#producer thread
def producer():
    print('I am the Producer')
    for i in range(10):
        with items_cv:
            items.append(i)
            items_cv.notify() 
        time.sleep(1)

#consumer thread
def consumer():
    print('I am Comnsumer ', threading.current_thread().name)
    while True:
        with items_cv:
            while not items:
                items_cv.wait() 
                # print('Nothing in buffer, but consumer will try to consume')
        x=items.pop(0)
        print(f'Consumer {threading.current_thread().name} consumed {x}')
        time.sleep(5)
    time.sleep(2)

cons = [threading.Thread(target=consumer)
        for i in range(3)]
for c in cons:
    c.setDaemon(True)
    c.start()
producer()
