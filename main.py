from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import shutil
from tkinter import filedialog
import tkinter.font

def clickEnt(args):
    ent.delete(0, 'end')


x = 0
def openImg(self):
    global x, filename, btnNext, btnBack, btnSizeON
     
    if x == 0:
        img = Image.open(path+everyFile[0])
    else:
        img = Image.open(path+everyFile[x])


    def Forward():
        global x, img
        x += 1
        try:
            SImg.grid_forget()
            BImg.grid_forget()
            img = Image.open(path+everyFile[x])
            openImg(self)
            
        except:
            x = -1
            Forward()
    
    
    def Backward():
        global x, img
        x -= 1
        try:
            SImg.grid_forget()
            BImg.grid_forget()
            img = Image.open(path+everyFile[x])
            openImg(self)

        except:
            x = 0
            Backward() 
       
    
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


    menu = StringVar(leftFrame)
    menu.set("1.0x")
    drop = OptionMenu(leftFrame, menu, "0.5x", "1.0x", "1.5x", "2.0x")
    drop.config(font = SmallFont, bg="#252422", fg="#ccc5b9",
                activebackground="#eb5e28", activeforeground="#ccc5b9")
    drop["menu"].config(bg="#252422", fg="#ccc5b9",
                        activebackground="#eb5e28", activeforeground="#ccc5b9")


    def imgSize(self):
            global width, height, img
            type = menu.get()
            img = Image.open(path+everyFile[x])
            width, height = img.size
            if type == "0.5x":
                widthB = int(width/3 * 0.5)
                heightB = int(height/3 * 0.5)
                
            elif type == "1.0x":
                widthB = int(width/3)
                heightB = int(height/3)
                
            elif type == "1.5x":
                widthB = int(width/3 * 1.5)
                heightB = int(height/3 * 1.5)
                
            elif type == "2.0x":
                widthB = int(width/3 * 2)
                heightB = int(height/3 * 2)
                
            
            imgB = img.resize((widthB, heightB))
            self.BigImg = ImageTk.PhotoImage(imgB)
            SImg.config(image=self.SmallImg)
            BImg.config(image=self.BigImg)


    entRename = Entry(leftFrame, textvariable=myStrV02)
    entRename.insert(0, 'Kép átnevezése és új mappába rakása')
    
    def fileCreate():
     
        oldFileName = path+everyFile[x]
        newFileName = path+entRename.get()

        newPath = path + "\." + "newFolder" 
        if not os.path.exists(newPath):
            os.makedirs(newPath)
            messagebox.showinfo("Mappa kész!", "Mappát sikeresen létrehozta!")
        elif os.path.exists(newPath):
            messagebox.showinfo("Hoppá!", "Ez a mappa már létezik")
            if os.path.isfile(newFileName):
                messagebox.showinfo("Valami nem jó!", "Ilyen nevű file már létezik.")
            os.rename(oldFileName, newFileName)
            shutil.move(newFileName, newPath)


    btnRename = Button(leftFrame, text="Átnevezés", command=fileCreate)

    SImg.grid(row=3, column=0, columnspan=3, padx=10, pady=5)
    BImg.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
    drop.grid(row=5, column=2)
    entRename.grid(row=8, column=0, columnspan=2)
    btnRename.grid(row=8, column=2)


    btnNext.config(text=">>", command=Forward)
    btnBack.config(text="<<", command=Backward)
    btnSizeON.config(text="Méretezés", command=lambda:[imgSize(self)])
    lbName.config(text=everyFile[x])
    entRename.config(font = SmallFont)

    
    

    


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



myStrV01 = StringVar()
myStrV02 = StringVar()
ent = Entry(leftFrame, textvariable=myStrV01)
ent.insert(0, 'Kérem nyomjon Entert')
ent.bind('<Return>', openPath)

btnInfo = Button(leftFrame, text="Infó")

lbTitle = Label(leftFrame, text="Képnézegető")
lbSize = Label(leftFrame, text="Képméret:")
lbName = Label(leftFrame, text="???")





btnNext = Button(leftFrame, text="")
btnBack = Button(leftFrame, text="")
btnSizeON = Button(leftFrame, text="")


leftFrame.grid(row=0, column=0, padx=10,  pady=5)
rightFrame.grid(row=0, column=1, padx=10,  pady=5)

lbTitle.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
lbSize.grid(row=5, column=0)
lbName.grid(row=7, column=0, columnspan=3, padx=10, pady=5)

ent.grid(row=2, column=0, columnspan=3, padx=10, pady=5)


btnBack.grid(row=4, column=0, padx=10, pady=5)
btnNext.grid(row=4, column=2, padx=10, pady=5)
btnInfo.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
btnSizeON.grid(row = 6, column=2)

lbTitle.config(font = TitleFont)
lbSize.config(font = SimpleFont)
lbName.config(font = SimpleFont) 

ent.config(font = SmallFont)


btnBack.config(font = SimpleFont)
btnNext.config(font = SimpleFont)
btnInfo.config(font = SimpleFont)
btnSizeON.config(font = SimpleFont)

root.mainloop()
