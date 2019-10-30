###########面向对象的经典GUI程序写法#############

# from tkinter import *
# from tkinter import messagebox
# import webbrowser


# class Application(Frame):
#     """一个经典的GUI程序"""
#     def __init__(self, master=None):
#         super().__init__(master)   # super()代表的是父类的定义，而不是父类对象，这里调用父类的构造方法
#         self.master = master
#         self.pack()
#         self.createWidget()
    
#     def createWidget(self):
#         """创建组件"""
#         self.v = StringVar()
#         self.v.set("F")
#         self.r1 = Radiobutton(root, text="male", value="M", variable=self.v)
#         self.r2 = Radiobutton(root, text="female", value="F", variable=self.v)

#         self.r1.pack(side="left");self.r2.pack(side="left")

#         Button(root, text="确定", command=self.confirm).pack(side="left")

#     def confirm(self):
#         messagebox.showinfo("测试", "选择的性别:"+self.v.get())

# if __name__ == "__main__":
#     root = Tk()
#     root.geometry("200x100+200+300")
#     root.title("一个经典形式的GUI程序")
#     app = Application(master=root)
#     root.mainloop()



from tkinter import *
from tkinter import messagebox
import webbrowser


class Application(Frame):
    """一个经典的GUI程序"""
    def __init__(self, master=None):
        super().__init__(master)   # super()代表的是父类的定义，而不是父类对象，这里调用父类的构造方法
        self.master = master
        self.pack()
        self.createWidget()
    
    def createWidget(self):
        """创建组件"""
        self.codeHobby = IntVar()
        self.videoHobby = IntVar()

        print(self.codeHobby.get())
        self.c1 = Checkbutton(self, text="敲代码",variable=self.codeHobby,onvalue=1,offvalue=0)
        self.c2 = Checkbutton(self, text="看视频",variable=self.videoHobby,onvalue=1,offvalue=0)

        self.c1.pack(side="left");self.c2.pack(side="left")
        Button(root, text="确定", command=self.confirm).pack(side="left")


    def confirm(self):
        if self.videoHobby.get() == 1:
            messagebox.showinfo("测试", "看视频，都是正常人有的爱好！你喜欢看什么类型？")
        if self.codeHobby.get() == 1:
            messagebox.showinfo("测试", "抓获野生程序员一只，赶紧送给他一坨...")
        

if __name__ == "__main__":
    root = Tk()
    root.geometry("200x100+200+300")
    root.title("一个经典形式的GUI程序")
    app = Application(master=root)
    root.mainloop()