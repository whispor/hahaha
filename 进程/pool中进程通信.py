from multiprocessing import Process, Queue, Pool, Manager
import multiprocessing
from time import sleep 

def write(q):
    a = ["a", "b", "c", "d"]
    for i in a:
        print("开始写入的值：%s"%i)
        q.put(i)
        sleep(1)

def reader(q):
    for i in range(q.qsize()):
        print("读取到的值：%s"%q.get())
        sleep(1)

if __name__ == "__main__":
    q = Manager().Queue()
    pool = Pool(3)
    pool.apply(write, (q,))
    pool.apply(reader, (q,))
    pool.close()
    pool.join()
