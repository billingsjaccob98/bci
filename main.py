__author__ = 'Jacob Billings & Allan Whatmough'

from Tkinter import *
from PIL import ImageTk, Image

class App(Frame):

    def __init__(self, master):
        Frame.__init__(self, master, width=100, height=100)
        frame = Frame(master)
        frame.pack()
        # button = Button(frame, text="QUIT", fg="red", command=frame.quit)

        # button.pack(side=LEFT)


        img = ImageTk.PhotoImage(Image.open("/Users/JacobBillings/PycharmProjects/bci/bci/icons/glyphicons-halflings-home.png"))
        # img = ImageTk.PhotoImage(Image.open("/Users/JacobBillings/PycharmProjects/bci/bci/icons/50x50.gif"))
        panel = Label(frame, image = img)
        panel.image = img
        panel.pack(side = "left", fill = "y")



root = Tk()

app = App(root)

app.master.title('BCI')

root.mainloop()
