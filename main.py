from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt" , filetypes=[("All Files" , "*.*") , ("Text Documents" , "*.txt")])

    if file == "":
        file = None

    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0,END)
        f = open(file , "r")
        TextArea.insert(1.0 , f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'untitled.txt' ,defaultextension=".txt" , filetypes=[("All Files" , "*.*") , ("Text Documents" , "*.txt")])

        if file == "":
            file =None

        else:
            f = open(file , "w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("About","Notepad by Vinutha")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("800x644")

    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    main_menu = Menu(root)

    file_menu = Menu(main_menu ,tearoff=0)
    file_menu.add_command(label="New",command=newFile)
    file_menu.add_command(label="Open", command=openFile)
    file_menu.add_command(label="Save", command=saveFile)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=quitApp)
    main_menu.add_cascade(label="File",menu=file_menu)

    edit_menu = Menu(main_menu ,tearoff=0)
    edit_menu.add_command(label="Cut", command=cut)
    edit_menu.add_command(label="Copy", command=copy)
    edit_menu.add_command(label="Paste", command=paste)
    main_menu.add_cascade(label="Edit", menu=edit_menu)

    help_menu = Menu(main_menu ,tearoff=0)
    help_menu.add_command(label="About Notepad", command=about)
    main_menu.add_cascade(label="Help", menu=help_menu)

    root.config(menu=main_menu)

    scrolly = Scrollbar(TextArea,cursor="arrow")
    scrolly.pack(side=RIGHT,fill=Y)
    scrolly.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrolly.set)

    root.mainloop()