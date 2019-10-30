#递归算法

# num = 1
# def a1():
#     global num
#     num += 1
#     print("a1")
#     print(num)
#     if num < 10:
#         a1()

# def b1():
#     print("b1")

# a1()

#使用递归计算阶乘
# print("请输入需要计算的数字：")
# num = int(input())
# def factorial(n):
#     print("第 {0} 次调用函数！".format(num-n+1))
#     if n == 1:
#         return n
#     else:
#         return n*factorial(n-1)
# result = factorial(num)
# print("{0} 的阶乘为：{1}".format(num, result))


#打印目录
import os

all_files = []
def getAllFiles(path,level):
    childeFlies = os.listdir(path)
    for file in childeFlies:
        filepath = os.path.join(path, file)
        # print(filepath)
        if os.path.isdir(filepath):
            getAllFiles(filepath, level+1)
        # print(filepath)
        all_files.append("\t"*level+filepath)

# getAllFiles(r"C:\Users\User\Desktop",0)
getAllFiles("testOS.py",0)

for f in all_files:
    print(f)