import threading,time

def create():
    print("Hello from %s" % (threading.current_thread().name))

threads = [threading.Thread(target=create) for _ in range(50)]
for t in threads[::-1]:
    t.start()
    time.sleep(1)
