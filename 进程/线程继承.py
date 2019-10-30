import multiprocessing
from multiprocessing import Process
import time
import random

class ClockProcess(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval
    
    def run(self):
        print("子进程开始执行的时间：{}".format(time.ctime()))
        time.sleep(self.interval)
        print("子进程结束的时间：{}".format(time.ctime()))

if __name__ == "__main__":
    # 创建进程
    t = random.randint(1,5)
    p = ClockProcess(t)
    # 启动进程
    p.start()
    p.join()
    print(t)
    print("进程结束")