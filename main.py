from tkinter import *
from PIL import ImageTk, Image
import tkinter.font

root = Tk()
root.title("Image Viewer")
root.eval('tk::PlaceWindow . center')

leftFrame = Frame(root, bg='red')
leftFrame.grid(row=0, column=0, padx=10,  pady=5)

rightFrame = Frame(root, bg='red')
rightFrame.grid(row=0, column=1, padx=10,  pady=5)


myStrV = StringVar()
ent = Entry(leftFrame, textvariable=myStrV)

btnNext = Button(leftFrame, text=">>")
btnBack = Button(leftFrame, text="<<")
btnInfo = Button(leftFrame, text="Infó")

lbTitle = Label(leftFrame, text="Képnézegető")
lbSize = Label(leftFrame, text="Képméret:")
lbName = Label(leftFrame, text="???")

menu = StringVar(leftFrame)
menu.set("Méret")
drop = OptionMenu(leftFrame, menu, "1.", "2.", "3.")
drop.config(bg="#252422", fg="#ccc5b9",
            activebackground="#eb5e28", activeforeground="#ccc5b9")
drop["menu"].config(bg="#252422", fg="#ccc5b9",
                    activebackground="#eb5e28", activeforeground="#ccc5b9")

type = menu.get()



lbTitle.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
lbSize.grid(row=4, column=0)
lbName.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

ent.grid(row=2, column=0, columnspan=3, padx=10, pady=5)
drop.grid(row=4, column=2)

btnBack.grid(row=3, column=0, padx=10, pady=5)
btnNext.grid(row=3, column=2, padx=10, pady=5)
btnInfo.grid(row=1, column=0, columnspan=3, padx=10, pady=5)







root.mainloop()
