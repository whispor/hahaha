###########布局管理器#############

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
        self.label01 = Label(self, text="用户名")
        self.label01.grid(row=0, column=0)
        self.entry01 = Entry(self)
        self.entry01.grid(row=0, column=1)
        Label(self, text="用户名为手机号").grid(row=0, column=2)

        Label(self, text="密码").grid(row=1,column=0)
        Entry(self, show="*").grid(row=1, column=1)

        Button(self, text="登录").grid(row=2, column=1, sticky=EW)
        Button(self, text="取消").grid(row=2, column=2, sticky=E)
        
root = Tk()
root.geometry("400x100+200+300")
root.title("一个经典形式的GUI程序")
app = Application(master=root)

root.mainloop()