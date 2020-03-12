from tkinter import *


class Btn_with_border():
    def __init__(self, parent):
        frame = Frame(parent, bd=0)

        #create canvas
        self.canvas1 = Canvas(frame, relief = FLAT, bg="red", width = 54, height = 50, bd=-2000, borderwidth=-2)
        # parametre de la grille
        self.canvas1.grid(row=0, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky=NW)
        #create canvas
        self.canvas2 = Canvas(frame, relief = FLAT, bg="red", width = 54, height = 50, bd=-2000, borderwidth=-2)
        # parametre de la grille
        self.canvas2.columnconfigure(0, weight = 0, pad = 20)
        self.canvas2.rowconfigure(0, weight = 0, pad = 20)
        self.canvas2.grid(row=0, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky=NW)
        #insere le bouton dans le canvas
        self.btn = Button(self.canvas1, text = "1", command = self.draw, width=5, height=2, relief=FLAT)
        self.btn2 = Button(self.canvas2, text = "3", command = self.draw2, width=5, height=2, relief=FLAT)

        self.btn.place(relx=0.5, rely=0.5, anchor=CENTER) #centre le bouton dans le canvas
        self.btn2.place(relx=0.5, rely=0.5, anchor=CENTER) #centre le bouton dans le canvas

        frame.configure(bg="blue")
        frame.pack()


    def draw(self):
        self.bdb()
        self.bdt()
        self.bdl()
        self.bdr()

    def draw2(self):
        self.btn.configure(bg = "green")
        self.canvas1.itemconfigure(self.canvas1, fill="green")

    def bbdt(self):
        self.canvas1.create_line(0, 2, 54, 2, width=5)
    def bbdb(self):
        self.canvas1.create_line(0, 48, 54, 48, width=4)
    def bbdr(self):
        self.canvas1.create_line(52, 0, 52, 54, width=4)
    def bbdl(self):
        self.canvas1.create_line(2, 0, 2, 50, width=5)

    def bdt(self):
        self.canvas1.create_line(0, 1, 54, 1, width=2)
    def bdb(self):
        self.canvas1.create_line(0, 49, 54, 49, width=2)
    def bdr(self):
        self.canvas1.create_line(53, 0, 53, 54, width=2)
    def bdl(self):
        self.canvas1.create_line(1, 0, 1, 54, width=2)


def main():
    root = Tk()
    root.geometry("600x450")
    app = Btn_with_border(root)
    root.mainloop()

if __name__ == '__main__':
    main()