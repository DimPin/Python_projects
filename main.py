from threading import Thread

def func(a):
    for i in range(5):
        print(f'It is {a} thread')

th1 = Thread(target=func, args = (1,))
th2 = Thread(target=func, args = (2,))
th3 = Thread(target=func, args = (3,))
th1.start()
th2.start()
th3.start()
th1.join()
th2.join()
th3.join()