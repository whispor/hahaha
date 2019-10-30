import multiprocessing
import time
import random

def func(msg):
    print("start:",msg)
    # print(msg+"将等待:"+haha+"秒！")
    time.sleep(3)
    print("end:",msg)

if __name__ == "__main__":
    # 创建进程池，并初始化容量
    pool = multiprocessing.Pool(3)
    # haha = random.randint(1, 5)
    #向池中天添加任务
    for i in range(1, 6):
        msg = "任务%d"%i
        pool.apply_async(func,(msg,))
    
    pool.close()
    pool.join()