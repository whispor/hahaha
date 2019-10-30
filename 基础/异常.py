import traceback

# try:
#     print("step1")
#     num = 1/0
# except:
#     traceback.print_exc()

#####将异常信息打印到指定文件####
try:
    print("step1")
    num = 1/0
except:
    with open("hehe.txt","a") as f:
        traceback.print_exc(file=f)