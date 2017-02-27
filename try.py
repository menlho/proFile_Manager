from tkinter import *

mygrey = '#3C3C3C'
darkgrey = '#333333'
root = Tk()
root.configure(background=darkgrey)
buttonfolder = Button(root,text = 'Click me',relief = FLAT,borderwidth = 12)
buttonfolder.configure(background=darkgrey ,activebackground = mygrey,highlightthickness = 0)
folderimage = PhotoImage(file = 'bin/folder_image.png')
buttonfolder.config(image = folderimage)
buttonfolder.pack()
root.mainloop()
