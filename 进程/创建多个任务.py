import multiprocessing
import time

def work1(interval):
    print("正在执行work1")
    time.sleep(interval)
    print("end work1")

def work2(interval):
    print("正在执行work2")
    time.sleep(interval)
    print("end work2")

def work3(interval):
    print("正在执行work1")
    time.sleep(interval)
    print("end work3")

if __name__ == "__main__":
    print("执行主进程")
    pool = []
    p1 = multiprocessing.Process(target=work1, args=(4,))
    p2 = multiprocessing.Process(target=work2, args=(2,))
    p3 = multiprocessing.Process(target=work3, args=(3,))
    pool.append(p1);pool.append(p2);pool.append(p3)
    # 调用子进程
    for p in pool:
        p.start()
        p.join()
    print("主进程结束!")
