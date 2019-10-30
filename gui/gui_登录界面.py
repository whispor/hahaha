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
        self.btn01 = Button(self, text="用户名")
        self.btn01.pack()

        # StringVar变量绑定到指定的组建
        # StringVar变量的值发生变化，组件内容也变化
        # 组建内容发生变化，StringVar变量的值也发生变化
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get());print(self.entry01.get())

        self.btn02 = Button(self, text="密码")
        self.btn02.pack()

        # StringVar变量绑定到指定的组建
        # StringVar变量的值发生变化，组件内容也变化
        # 组建内容发生变化，StringVar变量的值也发生变化
        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.pack()

        Button(self, text="登录", command=self.login).pack()


    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()
        print("进入数据库进行比对！")
        print("用户名："+username)
        print("密码："+pwd)

        if username=="haha" and pwd=="123456":
            messagebox.showinfo("hahahaha", "登录成功！")   # 参数：弹窗名，弹窗内容
        else:
            messagebox.showinfo("hahahaha","登录失败！用户名或密码错误！")

root = Tk()
root.geometry("400x150+200+300")
root.title("一个经典形式的GUI程序")
app = Application(master=root)

root.mainloop()