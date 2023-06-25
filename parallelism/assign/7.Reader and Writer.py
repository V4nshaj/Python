import threading,time, random
from threading import Lock
x = 0     # A shared value
COUNT = 5
lock = threading.Lock()

def reader():
    global x
    r=random.randint(1, 10)
    print(f"Reader is reading for {r} seconds!")
    lock.acquire()
    time.sleep(r)
    print("Shared data: ",x)
    lock.release()
def writer():
    global x
    r=random.randint(1, 10)
    print(f"Writer is writing for {r} seconds!")
    lock.acquire()
    time.sleep(r)
    x += 1
    print('Writer is Releasing the lock!')
    lock.release()
if __name__ == '__main__':
    for i in range(0, 10):
        randomNumber = random.randint(0, 20)   #Generate a Random number between 0 to 100
        if(randomNumber >9):
            Thread1 = threading.Thread(target = reader)
            Thread1.start()
            time.sleep(5)
        else:
            Thread2 = threading.Thread(target = writer)
            Thread2.start()
            time.sleep(5)
    Thread1.join()
    Thread2.join()
