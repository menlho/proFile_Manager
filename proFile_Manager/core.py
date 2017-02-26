import os
from tkinter import *
PathRoot = os.getcwd()
#print(os.getcwd())

##### DEV VALUES FOR ALPHA TESTING

##COLORS!!!!!!!!!!!!!!!!!!
mygrey = "#333333"
mydarkgrey  = "#3C3C3C"
CFinstance = 0  #variable that makes sure that only one instance of the Customer file can be summoned while it's running
FilesInfolder = []    ## self explanatory
FoldersInfolder = []
Paddingfolder = 25
imagefolder_path = "bin/folder_image.png"
imagefile_path = "bin/file_image.png"
foldery = 60
absfoldery = 0# the y axis of the 6 upcoming folders , mutable
shift = 0
mem = 0
firstmem = 0
lines = 0
#CORE OF DA CODE, DA WINDOW IS BELOW

#theses are shortcuts to type faster, makes also the code more readable...
def goto(path): #change the current directory to path
    os.chdir(path)
def here():    #returns the current working directory
    os.getcwd()
def isafile(something):
    if os.path.isfile(something):
        return True
    return False

def isafolder(something):
    if os.path.isdir(something):
        return True
    return False

def listdirectory():    ##this function will list folders and files in the directory
    global FoldersInfolder
    global FilesInfolder
    global imagefile_path
    global imagefolder_path
    global Paddingfolder
    global shift
    global Desk
    global foldery
    goto("Customer_Files/")
    here = os.getcwd()
    inhere = os.listdir(here)
    FilesInfolder = []    ## self explanatory
    FoldersInfolder = []
    Paddingfolder = 25

    for things in inhere:
        if isafile(things):
            FilesInfolder.append(things)
        else:
            FoldersInfolder.append(things)
    os.chdir(PathRoot)
    print(FoldersInfolder)
    print(len(FoldersInfolder))
    imagefolder_path = "bin/folder_image.png"
    imagefile_path = "bin/file_image.png"
    foldery = 60  # the y axis of the 6 upcoming folders , mutable
    shift = 0
    showthem()
def clicked(event):
    print("I got cliked !")
def showthem():
    global FoldersInfolder
    global FilesInfolder
    global imagefile_path
    global imagefolder_path
    global Paddingfolder
    global shift
    global Desk
    global foldery
    global absfoldery
    global mem
    global firstmem
    global lines
    absfoldery = foldery
    for elements in range((len(FoldersInfolder))):
        mem=elements+1
        if (elements % 6) == 0:
            lines = lines + 1
            foldery = absfoldery * lines * 2 - absfoldery
        folderImage = PhotoImage(file = "bin/folder_image.png")
        exec("""Desk.create_image(Paddingfolder*{} +64 + {}*70,foldery,image = folderImage,tags = 'click{}')""".format(((elements + mem) %6),((elements + mem) %6),elements))
        exec("""Desk.tag_bind('click{}','<Button-1>',clicked)""".format(elements))
    for elements in range((len(FilesInfolder))):
        if (elements + mem) % 6 == 0:
            lines = lines + 1
            foldery = absfoldery * lines * 2 - absfoldery
        fileImage = PhotoImage(file = "bin/file_image.png")
        exec("""Desk.create_image(Paddingfolder*{} +64 + {}*70,foldery,image = fileImage,tags = 'click{}')""".format(((elements + mem) %6),((elements + mem) %6),elements))
        exec("""Desk.tag_bind('click{}','<Button-1>',clicked)""".format(elements))
    mainloop()


def createCF():
    CF = "Customer_Files/"     #creates the path for the new Customer_Files
    os.chdir(CF)
    NewCF = open("Newfile",'w')
    NewCF.close()

def doNothing():
    print("didn't do anything")

##createCF()
##Here i build the windows that are going to be used in my code, i'll start with the
##Customer file window
def CFWindow():
    CFinstance = 1
    CFroot = Tk()
    CFroot.title("New Customer")
    LCF_Name = Label(CFroot,text = "Name")
    LCF_Name.grid(row =0 , column =0 )
    ECF_Name = Entry(CFroot)
    ECF_Name.grid(row =0 , column =1 )
    LCF_Surname = Label(CFroot,text = "Surname")
    LCF_Surname.grid(row =1 , column =0 )
    ECF_Surname = Entry(CFroot)
    ECF_Surname.grid(row =1 , column =1 )
    LCF_Mail1 = Label(CFroot,text = "Mail1")
    LCF_Mail1.grid(row =2 , column =0 )
    ECF_Mail1 = Entry(CFroot)
    ECF_Mail1.grid(row =2 , column =1 )
    LCF_Mail2 = Label(CFroot,text = "Mail2")
    LCF_Mail2.grid(row =3, column =0 )
    ECF_Mail2 = Entry(CFroot)
    ECF_Mail2.grid(row =3 , column =1 )
    LCF_Phone1 = Label(CFroot,text = "Phone1")
    LCF_Phone1.grid(row =4 , column =0 )
    ECF_Phone1 = Entry(CFroot)
    ECF_Phone1.grid(row =4 , column =1 )
    LCF_Phone2 = Label(CFroot,text = "Phone2")
    LCF_Phone2.grid(row =5 , column =0 )
    ECF_Phone2 = Entry(CFroot)
    ECF_Phone2.grid(row =5 , column =1 )
    LCF_Phone3 = Label(CFroot,text = "Phone3")
    LCF_Phone3.grid(row =6 , column =0 )
    ECF_Phone3 = Entry(CFroot)
    ECF_Phone3.grid(row =6 , column =1 )
    LCF_Adress = Label(CFroot,text = "Adress")
    LCF_Adress.grid(row =7 , column =0 )
    ECF_Adress = Entry(CFroot)
    ECF_Adress.grid(row =7 , column = 1)
    CFroot.mainloop()






##MAIN WINDOW
def MainWindow():
    Deskwidth = 600
    Deskheight = 800
    coreroot = Tk()
    coreroot.title("ProFile Manager")
    menu = Menu(coreroot)
    coreroot.config(menu = menu)
    ## MENU HEYHEYHEY!!!!!!!!!!!!!!!!!

    Topbar = Menu(menu)
    menu.add_cascade(label = "File",menu = Topbar)
    Topbar.add_command(label = "New customer file..",command = CFWindow)
    ##FILES ARE DISPLAYED HERE!!!!!!!!!!!!!!
    global Desk
    Desk = Canvas(width = Deskwidth,height = Deskheight, bg = mygrey)
    Desk.pack()
    listdirectory()


    coreroot.mainloop()

MainWindow()
