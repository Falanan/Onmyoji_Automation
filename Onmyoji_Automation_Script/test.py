import threading

def test_opt(x, y):
    for i in range(x, y):
        print(i)


thread1 = threading.Thread(name="T1", target=test_opt, args=(1, 10))
thread2 = threading.Thread(name="T2", target=test_opt, args=(11, 20))


thread1.start()
thread2.start()