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
        self.label01 = Label(self, text="hahaha", width=10, height=2, bg="blue", fg="white")
        self.label01.pack()
        self.label02 = Label(self, text="hohoho", width=10, height=2, bg="blue", fg="white")
        self.label02.pack()

        global photo # 将photo声明为全局变量
        photo = PhotoImage(file="image/2.gif")
        self.label03 = Label(self, image=photo)
        self.label03.pack()

        self.label04 = Label(self, text="hahaha\n hohohoh\n hehehhe\n joojjojojo", borderwidth=1, relief="solid", justify="right")
        self.label04.pack()


root = Tk()
root.geometry("400x400+200+300")
root.title("一个经典形式的GUI程序")
app = Application(master=root)

root.mainloop()