from multiprocessing import Process
import os
from time import sleep


def run_proc(name, age, **kwargs):
    for i in range(5):
        print("子进程运行中，参数name:%s, age:%d,"%(name, age))
        print("字典参数kwargs:",kwargs)
        sleep(0.5)


if __name__ == "__main__":
    print("主进程执行")
    # 创建子进程，target接受执行的任务
    p = Process(target=run_proc, args=("test", 18),kwargs={"m":23})
    print("子进程将要执行")
    # 调用子进程
    p.start()