from threading import Thread,current_thread
class mythread(Thread):
    def run(self):
        for x in range(3):
            print("Hi from child")
a = mythread()
a.start()
a.join()
print("Bye from",current_thread().getName())
