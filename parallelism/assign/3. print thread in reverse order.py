import threading, time

def create():
        print(f'Hello from {threading.current_thread().name}!')

cons = [threading.Thread(target=create)
        for i in range(50)]
for c in cons[::-1]:
    c.setDaemon(True)
    c.start()
    time.sleep(1)