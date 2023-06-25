import threading, random, time

class Philosopher(threading.Thread):
    def think(self,ttime):
        time.sleep(ttime)
    def eat(self,etime):
        time.sleep(etime)
    
    def diningphil(self, phil,chl,chr,rand):
        print(f'Philosopher {phil} is starting')
        thinkTime=random.randint(1, rand)
        eatTime=random.randint(1, rand+1)
        print(f'Philospher {phil} is thinking for {thinkTime} sec')
        self.think(thinkTime)
        print(f'Philospher {phil} is asking for chopstick')
        chl.acquire()
        print(f'Philospher {phil} got chopstick')
        self.think(1)
        print(f'Philospher {phil} is asking for chopstick')
        chr.acquire()
        print(f'Philospher {phil} got chopstick')
        print(f'Philospher {phil} is eating for {eatTime} sec')
        print(f'Philospher {phil} is releasing chopstick')
        chl.release()
        chr.release()
        print(f'Philospher {phil} is finished')

if __name__ =='__main__':
    job=[]
    forks=[threading.Semaphore() for n in range(5)]
    phil=Philosopher()
    for i in range(2):
        x=threading.Thread(target=phil.diningphil,args=(i+1, forks[i%2], forks[(i+1)%2], 10))
        job.append(x)
        x.start()
        x.join()