import multiprocessing
import time


def clock(interval):
    for i in range(3):
        print("当前事件：{}".format(time.ctime()))
        time.sleep(interval)

if __name__ == "__main__":
    p = multiprocessing.Process(target=clock, args=(1,))
    p.start()
    print("p.id:", p.pid)
    print("p.name:", p.name)
    print("p.is_alive:", p.is_alive())
