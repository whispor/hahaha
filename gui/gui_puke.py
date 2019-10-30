from tkinter import *

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    
    def createWidget(self):
        """通过place布局实现"""
        # self.photo = PhotoImage(file="image/poker1,gif")
        # self.poker1 = Label(self, image=photo)
        # self.poker1.place(x=10, y=50)

        self.photos = [PhotoImage(file="image/"+str(i+1)+".gif") for i in range(5)]
        self.pokers = [Label(self.master, image=self.photos[i]) for i in range(5)]

        for i in range(5):
            self.pokers[i].place(x=10+i*70,y=80)

        # 为label增加事件处理
        self.pokers[0].bind_class("Label", "<Button-1>", self.chupai)

    def chupai(self, event):
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_y())

        if event.widget.winfo_y() == 80:
            event.widget.place(y=50)
        else:
            event.widget.place(y=80)

if __name__ == "__main__":
    root = Tk()
    root.geometry("700x500+200+300")
    app = Application(master=root)
    root.mainloop()