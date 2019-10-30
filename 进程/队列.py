from multiprocessing import Queue 

# 默认队列数量不限，指定为3个
q = Queue(3)
# 向队列中插入
q.put("haha1")
q.put("haha2")
q.put("haha3")

# put方法中可选参数
# q.put("haha4", block=True, timeout=1) # 如果队列已满，等待1s，如果还是满的就抛出队列已满的异常
# 判断当前队列是否已满
print("判断当前队列是否已满：", q.full())
if not q.full():
    q.put("haha4", block=True, timeout=1)

# print(q.get())
# print(q.get())
# print(q.get())
# if not q.empty():
#     print(q.get(block=True, timeout=1))

# 查看队列的大小
print("队列的大小：", q.qsize())

for i in range(q.qsize()):
    print(q.get())