import os
from Tkinter import *
from turtle import *
import PIL
from PIL import Image,ImageTk
PathRoot = os.getcwd()
#print(os.getcwd())

##### DEV VALUES FOR ALPHA TESTING

##COLORS!!!!!!!!!!!!!!!!!!
mygrey = "#333333"
mydarkgrey  = "#3C3C3C"
CFinstance = 0  #variable that makes sure that only one instance of the Customer file can be summoned while it's running


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

def listdirectory():      ##this function will list folders and files in the directory
    goto("Customer_Files/")
    here = os.getcwd()
    inhere = os.listdir(here)
    FilesInfolder = []    ## self explanatory
    FoldersInfolder = []
    Counthere = 0
    for things in inhere:
        Counthere += 1
        if isafile(things):
            FilesInfolder.append(things)

        else:
            FoldersInfolder.append(things)
    os.chdir(PathRoot)
    Paddingfolder = 26
    image_path = "bin/folder_image.png"
    scale_y = 0 #position of the image y axis, evolve with elements
    scale_x = 0 #position of the image x axis, evolve with elements (in iteration)
    for elements in range(0,len(FoldersInfolder)):
        
        if elements == 6 or elements == 12 or elements == 18 or elements == 24:
            #here it allows the images to jump on the 2nd line, in order to create a 6 x X grid
            scale_y= 0
            scale_x = 0

        if elements <= 5 :
            #Align folder icons on a 6x1 grid

            exec "Apngfolder%s= Image.open(image_path)" % (elements)
            exec "Bpngfolder%s= ImageTk.PhotoImage(Apngfolder%s)" % (elements, elements)
            exec "Cpngfolder%s= Desk.create_image(26+35+Paddingfolder*%s + %s*70, 80, image=Bpngfolder%s)" % (elements,scale_x,scale_y,elements)
            scale_y += 1
            scale_x += 1

        if elements > 5 and elements <= 11:
            #conditions to place the 2nd line of the grid
            exec "Apngfolder%s= Image.open(image_path)" % (elements)
            exec "Bpngfolder%s= ImageTk.PhotoImage(Apngfolder%s)" % (elements, elements)
            exec "Cpngfolder%s= Desk.create_image(26+35+Paddingfolder*%s + %s*70, 160, image=Bpngfolder%s)" % (elements,scale_x,scale_y,elements)
            scale_y += 1
            scale_x += 1
        if elements > 11 and elements <= 17:
            #conditions to place the 2nd line of the grid
            exec "Apngfolder%s= Image.open(image_path)" % (elements)
            exec "Bpngfolder%s= ImageTk.PhotoImage(Apngfolder%s)" % (elements, elements)
            exec "Cpngfolder%s= Desk.create_image(26+35+Paddingfolder*%s + %s*70, 240, image=Bpngfolder%s)" % (elements,scale_x,scale_y,elements)
            scale_y += 1
            scale_x += 1
        if elements > 17 and elements <= 23:
            #conditions to place the 2nd line of the grid
            exec "Apngfolder%s= Image.open(image_path)" % (elements)
            exec "Bpngfolder%s= ImageTk.PhotoImage(Apngfolder%s)" % (elements, elements)
            exec "Cpngfolder%s= Desk.create_image(26+35+Paddingfolder*%s + %s*70, 320, image=Bpngfolder%s)" % (elements,scale_x,scale_y,elements)
            scale_y += 1
            scale_x += 1

    mainloop()



# Apngfolder = Image.open("bin/folder_image.png")
# Bpngfolder = ImageTk.PhotoImage(Apngfolder)
# Cpngfolder = Desk.create_image(100, 80, image=Bpngfolder)



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
    global CFinstance
    if CFinstance == 1:
        pass
    else:
        CFinstance= 1
        CFroot = Tk()
        CFroot.title("New Customer")
        LCFname = Label(CFroot,text = "Name")
        LCFname.pack()
        LCFSurname = Label(CFroot,text = "Surname")
        LCFSurname.pack()
        LCFMail = Label(CFroot,text = "Mail")
        LCFMail.pack()
        LCFnumber = Label(CFroot,text = "Number")
        LCFnumber.pack()
        LCFAdress = Label(CFroot,text = "Adress")
        LCFAdress.pack()
        CFroot.mainloop()
        CFinstance = 0
##MAIN WINDOW
def MainWindow():
    global Deskwidth
    Deskwidth = 600
    global Deskheight
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
