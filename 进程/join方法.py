from multiprocessing import Process
import os
from time import sleep


def worker(interval):
    print("work start")
    sleep(interval)
    print("work end")

if __name__ == "__main__":
    print("主进程正在执行")
    p = Process(target=worker, args=(5,))
    p.start()
    p.join()  # 希望下面的输出语句，在子进程执行完才输出，则必须join()的参数>子进程的参数，即args中的参数
    print("主进程执行完毕！")