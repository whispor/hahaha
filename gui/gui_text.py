###########面向对象的经典GUI程序写法#############

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
        self.w1 = Text(root, width=65, height=20, bg="white")
        self.w1.pack()
        self.w1.insert(1.0, "0123456789\nabcdefg")
        self.w1.insert(2.3, "哈哈哈哈，呵呵呵呵，嘿嘿嘿嘿，吼吼吼吼\n")

        Button(self, text="重复插入文本",command=self.insertText).pack(side="left")
        Button(self, text="返回文本",command=self.returnText).pack(side="left")
        Button(self, text="添加图片",command=self.addImage).pack(side="left")
        Button(self, text="添加组件",command=self.addWidget).pack(side="left")
        Button(self, text="通过Tag精确控制文本",command=self.testTag).pack(side="left")

    def insertText(self):
        self.w1.insert(INSERT, ' haha ')
        self.w1.insert(END, '[sxt]')

    def returnText(self):
        print(self.w1.get(1.2, 1.6))
        self.w1.insert(1.8, "haha")
        print("所有文本内容：\n"+self.w1.get(1.0, END))
    
    def addImage(self):
        self.photo = PhotoImage(file="image/2.gif")
        self.w1.image_create(END, image=self.photo)
    
    def addWidget(self):
        b1 = Button(self.w1, text="haha")
        self.w1.window_create(INSERT, window=b1)

    def testTag(self):
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, "good good study, day day up!\nhahahaha\nhehehehe\heiheiheihei\nhohohoho")
        self.w1.tag_add("good", 1.0, 1.9)
        self.w1.tag_config("good", background="yellow", foreground="red")
        
        self.w1.tag_add("baidu", 4.0, 4.2)
        self.w1.tag_config("baidu", underline=True)
        self.w1.tag_bind("baidu", "<Button-1>", self.webshow)

    def webshow(self,event):
        webbrowser.open("http://www.baidu.com")

if __name__ == "__main__":
    root = Tk()
    root.geometry("450x300+200+300")
    root.title("一个经典形式的GUI程序")
    app = Application(master=root)
    root.mainloop()