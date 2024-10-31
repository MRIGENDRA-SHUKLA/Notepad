from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("500x450")
root.title("NOTEPAD")

menubar = Menu(root)

def openfile():
    f = filedialog.askopenfile()
    print(f.read())

menubar = Menu(menubar)

## file menu 
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

## FILE sub menu
filemenu.add_command(label="New File")
filemenu.add_command(label="Save", command=openfile)
filemenu.add_command(label="Exit", command=exit)

###---Edit Menu
editemenu=Menu(menubar,tearoff=0 )
menubar.add_cascade(label="Edit",menu=editemenu)

editemenu.add_command(label="Undo")
editemenu.add_command(label="Cut")
editemenu.add_command(label="Copy")
editemenu.add_command(label="Paste")
editemenu.add_command(label="Delete")

###---View Menu
Viewemenu=Menu(menubar,tearoff=0 )
menubar.add_cascade(label="View",menu=Viewemenu )

Viewemenu.add_command(label="Zoom")
Viewemenu.add_command(label="Status Bar")
Viewemenu.add_command(label="Wrap up")


root.config(menu=menubar)

## Text Widget with Scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

text = Text(frame, wrap="none", width=40, height=20)
text.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(frame, orient="vertical", command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)

text.config(yscrollcommand=scrollbar.set)

root.config(menu=menubar)
root.mainloop()