from tkinter import *


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Layout Test")
        self.config()
        self.pack()

        #create canvas
        canvas1 = Canvas(self, relief = FLAT, background = "red", width = 100, height = 100)
        canvas1.pack()

        button1 = Button(self, text = "1", command = self.quit, width=5, height=2)
        button1.configure()
        button1.pack()
        canvas1.create_window(0, 0, window = button1, anchor=NW)

def main():
    root = Tk()
    root.geometry('800x600+10+50')
    app = Example(root)
    app.mainloop()

if __name__ == '__main__':
    main()