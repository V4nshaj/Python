import threading, time
capacity=10
buffer=[-1 for i in range(capacity)]
in_index=0
out_index=0
mutex=threading.Semaphore()
empty=threading.Semaphore(capacity)
full=threading.Semaphore(0)
class Producer(threading.Thread):
    def run(self):
        global capacity,buffer,in_index, out_index
        global mutex, empty, full
        item_produced=0
        counter=0
        while item_produced<10:
            empty.acquire()
            mutex.acquire()
            counter+=1
            buffer[in_index]=counter
            in_index=(in_index+1)%capacity
            print("Producer produced: ", counter)
            mutex.release()
            full.release()
            time.sleep(1)
            item_produced+=1
#consumer Thread class
class Consumer(threading.Thread):
    def run(self):
        global capacity,buffer,in_index, out_index,counter
        global mutex, empty, full
        item_consumed=0
        while item_consumed<10:
            full.acquire()
            mutex.acquire()
            item=buffer[out_index]
            out_index=(out_index+1)%capacity
            print('Consumer consumed item: ', item)
            mutex.release()
            empty.release()
            time.sleep(3)
            item_consumed +=1
producer=Producer()
consumer=Consumer()
consumer.start()
producer.start()
producer.join()
consumer.join()