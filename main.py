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
        ent.delete(0, END)
        ent.insert(0, path+everyFile[0])
        root.title("Image Viewer (%s)" % everyFile[x])
    else:
        img = Image.open(path+everyFile[x])
        ent.delete(0, END)
        ent.insert(0, path+everyFile[x])
        root.title("Image Viewer (%s)" % everyFile[x])

    def Forward():
        global x, img
        x += 1
        try:
            SImg.grid_forget()
            BImg.grid_forget()
            img = Image.open(path+everyFile[x])
            ent.delete(0, END)
            ent.insert(0, path+everyFile[x])
            root.title("Image Viewer (%s)" % everyFile[x])
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
            ent.delete(0, END)
            ent.insert(0, path+everyFile[x])
            root.title("Image Viewer (%s)" % everyFile[x])
            openImg(self)

        except:
            x = 0
            Backward()

    width, height = img.size
    if width >= height:
        ent.grid_configure(ipadx=85)
    else:
        ent.grid_configure(ipadx=35)
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
    drop = OptionMenu(leftFrame, menu, "0.2x", "0.5x",
                      "1.0x", "1.5x", "2.0x", "2.5x", "3.0x")
    drop.config(font=SmallFont, bg="#161521", fg="#ed6165",
                activebackground="#2D2A49", activeforeground="#82b1c4", highlightthickness=0)
    drop["menu"].config(bg="#161521", fg="#ed6165",
                        activebackground="#2D2A49", activeforeground="#82b1c4")

    def imgSize(self):

        global width, height, img
        type = menu.get()
        img = Image.open(path+everyFile[x])
        width, height = img.size
        if type == "0.2x":
            widthB = int(width/3 * 0.2)
            heightB = int(height/3 * 0.2)

        elif type == "0.5x":
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

        elif type == "2.5x":
            widthB = int(width/3 * 2.5)
            heightB = int(height/3 * 2.5)

        elif type == "3.0x":
            widthB = int(width/3 * 3)
            heightB = int(height/3 * 3)

        imgB = img.resize((widthB, heightB))
        self.BigImg = ImageTk.PhotoImage(imgB)
        SImg.config(image=self.SmallImg)
        BImg.config(image=self.BigImg)

    def delEntContent(args):
        entRename.delete(0, 'end')
    entRename = Entry(leftFrame, textvariable=myStrV02)
    entRename.insert(0, 'K??p ??tnevez??se ??s ??j mappa')
    entRename.bind('<Button-1>', delEntContent)

    def fileCreate():

        oldFileName = path+everyFile[x]
        newFileName = path+entRename.get()

        newPath = path + "\." + "newFolder"
        if not os.path.exists(newPath):
            os.makedirs(newPath)
            messagebox.showinfo("Mappa k??sz!", "Mapp??t sikeresen l??trehozta!")
        elif os.path.exists(newPath):
            if os.path.isfile(newFileName):
                messagebox.showerror("Valami nem j??!", "Nem tudom ??th??zni a f??jlt a mapp??ba...\nVizsg??lja meg az al??bbi lehet??s??geket:\n\t1.: L??tezik olyan file, ami egyezik az ??t??rni k??v??nt file nev??vel a '%s.newFolder/' mapp??ban\n\t2.: L??tezik olyan file, ami egyezik az ??t??rni k??v??nt file nev??vel a '%s' mapp??ban" % (path, path))
            try:
                os.rename(oldFileName, newFileName)
                shutil.move(newFileName, newPath)
            except shutil.Error:
                messagebox.showerror(
                    "Valami nem j??!", "Ilyen nev?? file m??r l??tezik.\nNem tudom ??th??zni a mapp??ba\nA file az eredeti mapp??ban lett ??tnevezve")

    btnRename = Button(leftFrame, text="??tnevez??s", command=fileCreate)

    SImg.grid(row=3, column=0, columnspan=3, padx=10, pady=5)
    BImg.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
    drop.grid(row=5, column=2)
    entRename.grid(row=8, column=0, columnspan=2, ipadx=30)
    btnRename.grid(row=8, column=2)

    btnNext.config(text=">>", command=Forward, bg="#161521", fg="#ed6165",
                   activebackground="#2D2A49", activeforeground="#82b1c4", border=0)
    btnBack.config(text="<<", command=Backward, bg="#161521", fg="#ed6165",
                   activebackground="#2D2A49", activeforeground="#82b1c4", border=0)
    btnSizeON.config(text="M??retez??s", command=lambda: [imgSize(
        self)], bg="#161521", fg="#ed6165", activebackground="#2D2A49", activeforeground="#82b1c4", border=0)
    btnRename.config(font=SimpleFont, bg="#161521", fg="#ed6165",
                     activebackground="#2D2A49", activeforeground="#82b1c4", border=0)

    lbName.config(text=everyFile[x], bg="#161521", fg="#ed6165")
    entRename.config(font=SmallFont, bg="#2D2A49", fg="#82b1c4")


def entPrint(self):
    ent.delete(0, END)
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
    root2.resizable(False, False)
    root2.eval('tk::PlaceWindow . center')
    root2.configure(bg="#161521")

    Choose = Label(root2, text="Szeretn??l m??g egy k??pet beh??zni?")
    btnYes = Button(root2, text="Igen", command=lambda: [
                    openPath(self), root2.destroy()])
    btnNo = Button(root2, text="Nem", command=lambda: [
                   entPrint(self), root2.destroy()])

    Choose.grid(row=0, column=0, columnspan=2)
    btnYes.grid(row=1, column=0, padx=5, pady=10)
    btnNo.grid(row=1, column=1, padx=5, pady=10)

    Choose.config(font=('Courier new', 20, 'bold'), bg="#161521", fg="#ed6165",
                  activebackground="#2D2A49", activeforeground="#82b1c4", border=0)
    btnYes.config(font=('Courier new', 12), bg="#161521", fg="#ed6165",
                  activebackground="#2D2A49", activeforeground="#82b1c4", border=0)
    btnNo.config(font=('Courier new', 12), bg="#161521", fg="#ed6165",
                 activebackground="#2D2A49", activeforeground="#82b1c4", border=0)


root = Tk()
root.title("Image Viewer")
root.eval('tk::PlaceWindow . center')
root.configure(bg="#161521")

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
ent.insert(0, 'K??rem nyomjon Entert')
ent.bind('<Return>', openPath)


def openInfo():
    root_info = Tk()
    root_info.title("Inform??ci??")
    root_info.resizable(False, False)
    root_info.eval('tk::PlaceWindow . center')
    root_info.configure(bg="#161521")

    info_Title = Label(root_info, text="Haszn??lati utas??t??s")
    info1 = Label(root_info, text=".png; .jpg; .gif; k??p kiterjeszt??st elfogad import??l??s sor??n a program.\nK??pes vagy beimport??lni t??bb k??pet is, ??s m??ret??ket ??s nev??ket v??ltoztatni tudod.\nK??pm??ret v??ltoztat??sn??l CSAK a programban v??ltozik a k??p m??rete.\nAmikok m??dos??tani akarod a file nev??t, K??ZELEZ?? ut??na ??rni a k??v??nt kiterjeszt??st.\nHa sikeresen ??tnevezted a f??jlod, akkor egy .newFolder mappa (+m??dos??tott k??p a tartalma) fog abban a mapp??ban megjelenni, ahol az eredeti k??p volt.")

    infoBtn = Button(root_info, text="Vissza", command=root_info.destroy)

    info_Title.grid(row=0, column=0, padx=20, sticky=EW)
    info1.grid(row=1, pady=15, column=0, padx=20, sticky=EW)
    infoBtn.grid(row=2, column=0)

    info_Title.config(anchor=CENTER, font=(
        'Courier new', 20, 'bold'), bg="#161521", fg="#ed6165")
    info1.config(anchor=CENTER, font=('Courier new', 12),
                 bg="#161521", fg="#ed6165")
    infoBtn.config(anchor=CENTER, font=('Courier new', 12), bg="#161521", fg="#ed6165",
                   activebackground="#2D2A49", activeforeground="#82b1c4", border=0)


btnInfo = Button(leftFrame, text="Inf??", command=openInfo)

lbTitle = Label(leftFrame, text="K??pn??zeget??")
lbSize = Label(leftFrame, text="K??pm??ret:")
lbName = Label(leftFrame, text="???")


btnNext = Button(leftFrame, text="")
btnBack = Button(leftFrame, text="")
btnSizeON = Button(leftFrame, text="")


leftFrame.grid(row=0, column=0, padx=10,  pady=5)
rightFrame.grid(row=0, column=1, padx=10,  pady=5)

lbTitle.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
lbSize.grid(row=5, column=0, columnspan=2, sticky=E)
lbName.grid(row=7, column=0, columnspan=3, padx=10, pady=5)

ent.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

btnBack.grid(row=4, column=0, padx=10, pady=5)
btnNext.grid(row=4, column=2, padx=10, pady=5)
btnInfo.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
btnSizeON.grid(row=6, column=2)

leftFrame.config(bg="#161521")
rightFrame.config(bg="#161521")


lbTitle.config(font=TitleFont, bg="#161521", fg="#ed6165")
lbSize.config(font=SimpleFont, bg="#161521", fg="#ed6165")
lbName.config(font=SimpleFont, bg="#161521", fg="#ed6165")

ent.config(font=SmallFont, bg="#2D2A49", fg="#82b1c4")


btnBack.config(font=SimpleFont, bg="#161521", fg="#ed6165",
               activebackground="#2D2A49", activeforeground="#82b1c4", border=0)
btnNext.config(font=SimpleFont, bg="#161521", fg="#ed6165",
               activebackground="#2D2A49", activeforeground="#82b1c4", border=0)
btnInfo.config(font=SimpleFont, bg="#161521", fg="#ed6165",
               activebackground="#2D2A49", activeforeground="#82b1c4", border=0)
btnSizeON.config(font=SimpleFont, bg="#161521", fg="#ed6165",
                 activebackground="#2D2A49", activeforeground="#82b1c4", border=0)

root.mainloop()
