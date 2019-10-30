import os

# # os.system("ping www.baidu.com")
# # os.system("chrome.exe")
# # os.system("cmd")
# os.startfile(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")

all_files = []
path = os.getcwd()
list_files = os.walk(path)
for dirpath, dirnames, filenames in list_files:
    for dir in dirnames:
        all_files.append(os.path.join(dirpath, dir))
        # print((os.path.join(dirpath, dir))
    for file in filenames:
        all_files.append(os.path.join(dirpath, file))
        # print(os.path.join(dirpath, file))

for file in all_files:
    print(file)