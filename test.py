from tkinter import *
from grille import Grille


class Btn():
    def __init__(self, parent):
        frame = Frame(parent)

        #create canvas
        self.canvas1 = Canvas(frame, relief = FLAT, bg="red", width = 54, height = 50)
        self.canvas1.grid()

        #insere le bouton dans le canvas
        self.btn = Button(self.canvas1, text = "1", command = self.draw, width=5, height=2, relief=FLAT)

        self.btn.place(relx=0.5, rely=0.5, anchor=CENTER) #centre le bouton dans le canvas
        frame.grid()

    def draw(self):
        self.bbdb()
        self.bdt()
        self.bdl()
        self.bdr()

    def bbdt(self):
        self.canvas1.create_line(0, 4, 58, 4, width=5)
    def bbdb(self):
        self.canvas1.create_line(0, 50, 58, 50, width=4)
    def bbdr(self):
        self.canvas1.create_line(54, 0, 54, 54, width=4)
    def bbdl(self):
        self.canvas1.create_line(4, 0, 4, 54, width=5)

    def bdt(self):
        self.canvas1.create_line(0, 2, 58, 2, width=4)
    def bdb(self):
        self.canvas1.create_line(0, 52, 54, 52, width=4)
    def bdr(self):
        self.canvas1.create_line(56, 0, 56, 54, width=4)
    def bdl(self):
        self.canvas1.create_line(2, 0, 2, 54, width=4)


def main():
    root = Tk()
    root.geometry("600x450")
    app = Btn(root)
    root.mainloop()

if __name__ == '__main__':
    main()