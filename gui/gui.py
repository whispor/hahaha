from tkinter import *
from tkinter import messagebox


root = Tk()

root.title("哦哈哈哈！")  # 窗口名称
root.geometry("500x300+100+200")  # 窗口大小和位置


btn01 = Button(root)   # 创建一个按钮，并放到窗口中
btn01["text"] = "点击就屠龙刀"    # 按钮名字

btn01.pack()   # 调用布局管理器

def zengsong(e): # e就是事件对象，定义事件的行为
    messagebox.showinfo("Message", "送你一本武林秘籍！")
    print("hahahaha,牛逼！")

btn01.bind("<Button-1>",zengsong)  # 将按钮和事件进行绑定，<Button-1>为左键单击

root.mainloop()  # 调用组建的mainloop()方法，进入事件循环