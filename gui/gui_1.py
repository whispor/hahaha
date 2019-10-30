###########面向对象的经典GUI程序写法#############

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的GUI程序"""
    def __init__(self, master=None):
        super().__init__(master)   # super()代表的是父类的定义，而不是父类对象，这里调用父类的构造方法
        self.master = master
        self.pack()

        self.createWidget()
    
    def createWidget(self):
        """创建组件"""
        # self.btn01 = Button(self)
        # self.btn01["text"] = "点击就送"
        # self.btn01.pack()
        # self.btn01["command"] = self.songhua
        self.btn01 = Button(self, text="点击就送", command=self.songhua)
        self.btn01.pack()

        # 创建一个退出按钮
        self.btnQuit = Button(self, text="退出", command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("送花", "23333333")

root = Tk()
root.geometry("400x200+200+300")
root.title("一个经典形式的GUI程序")
app = Application(master=root)

root.mainloop()