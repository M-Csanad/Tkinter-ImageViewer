from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.font

root = Tk()
root.title("Image Viewer")
root.eval('tk::PlaceWindow . center')

TitleFont = tkinter.font.Font(
    family='Courier new',
    weight='bold',
    size=20,
)

SimpleFont = tkinter.font.Font(
    family='Courier new',
    size=12,
)

SmallFont = tkinter.font.Font(
    family='Courier new',
    size=9,
)



leftFrame = Frame(root, bg='red')
rightFrame = Frame(root, bg='red')



def clickEnt(args):
    ent.delete(0, 'end')

myStrV = StringVar()
ent = Entry(leftFrame, textvariable=myStrV)
ent.insert(0, 'Kérem nyomjon Entert')


btnNext = Button(leftFrame, text=">>")
btnBack = Button(leftFrame, text="<<")
btnInfo = Button(leftFrame, text="Infó")

lbTitle = Label(leftFrame, text="Képnézegető")
lbSize = Label(leftFrame, text="Képméret:")
lbName = Label(leftFrame, text="???")

menu = StringVar(leftFrame)
menu.set("Méret")
drop = OptionMenu(leftFrame, menu, "1.", "2.", "3.")
drop.config(font = SmallFont, bg="#252422", fg="#ccc5b9",
            activebackground="#eb5e28", activeforeground="#ccc5b9")
drop["menu"].config(bg="#252422", fg="#ccc5b9",
                    activebackground="#eb5e28", activeforeground="#ccc5b9")

type = menu.get()



def openImg(self):
    global filename
    img = Image.open(path+filename)
    width, height = img.size

    widthS = int(width/10)
    heightS = int(height/10)
    imgS = img.resize((widthS, heightS))
    self.SmallImg = ImageTk.PhotoImage(imgS)

    widthB = int(width/3)
    heightB = int(height/3)
    imgB = img.resize((widthB, heightB))
    self.BigImg = ImageTk.PhotoImage(imgB)

    SImg = Label(leftFrame, image=self.SmallImg)
    BImg = Label(rightFrame,  image=self.BigImg)


    SImg.grid(row=3, column=0, columnspan=3, padx=10, pady=5)
    BImg.grid(row=0, column=0, columnspan=3, padx=10, pady=5)


def entPrint(self):    
    ent.delete(0, END)
    ent.insert(0, path+filename)
    ent.bind("<Return>", lambda: clickEnt(self), openImg(self))

everyFile = []
def openPath(self):
    global path, filename
    Fullpath = filedialog.askopenfilename(title='open')
    pathSlice = Fullpath.split("/")
    a = []
    path = ""
    for i in range(len(pathSlice)-1):
        a.append(pathSlice[i])
    for x in a:
        path += x + "/"    

    filename = pathSlice[-1]
    everyFile.append(filename)

    root2 = Tk()
    root2.title("Continue?")
    root2.eval('tk::PlaceWindow . center')
    Choose = Label(root2, text="Szeretnél még egy képet behúzni?") 
    btnYes = Button(root2, text="Igen", command=lambda:[openPath(self), root2.destroy()])
    btnNo = Button(root2, text="Nem", command=lambda:[entPrint(self), root2.destroy()])
    

    Choose.grid(row=0, column=0, columnspan=2)
    btnYes.grid(row=1, column=0, padx=5, pady=10)
    btnNo.grid(row=1, column=1, padx=5, pady=10)

    Choose.config(font = TitleFont)
    btnYes.config(font = SimpleFont)
    btnNo.config(font = SimpleFont)   

    
ent.bind('<Return>', openPath)


leftFrame.grid(row=0, column=0, padx=10,  pady=5)
rightFrame.grid(row=0, column=1, padx=10,  pady=5)

lbTitle.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
lbSize.grid(row=5, column=0)
lbName.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

ent.grid(row=2, column=0, columnspan=3, padx=10, pady=5)
drop.grid(row=5, column=2)

btnBack.grid(row=4, column=0, padx=10, pady=5)
btnNext.grid(row=4, column=2, padx=10, pady=5)
btnInfo.grid(row=1, column=0, columnspan=3, padx=10, pady=5)


lbTitle.config(font = TitleFont)
lbSize.config(font = SimpleFont)
lbName.config(font = SimpleFont) 

ent.config(font = SmallFont)

btnBack.config(font = SimpleFont)
btnNext.config(font = SimpleFont)
btnInfo.config(font = SimpleFont)

root.mainloop()
