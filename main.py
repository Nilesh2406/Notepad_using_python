from logging import root
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
import os
def newFile():
 global file
 root.title("untitled - Notepad")
 file = None
 TextArea.delete(1.0,END)
def openFile():
 global file
 file = askopenfilename(defaultextension=".txt",
 filetypes=[("All Files", "*.*"),
 ("Text Documents",
 "*.txt")])
 if file =="":
   file=None
 else:
    root.title(os.path.basename(file) + " - Notepad")
    TextArea.delete(1.0,END)
    f =open(file,"r")
    TextArea.insert(1.0,f.read())
    f.close()
def saveFile():
 global file
 if file==None:
    file=asksaveasfilename(initialfile='untitled.txt',defaultextension=".txt",
    filetypes=[("All Files","*.*"),
    ("Text Documents",
    "*.txt")])
    if file=="":
        file=None
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close
        root.title(os.path.basename(file)+ "- Notepad")
        print("file saved")
 else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close   
def quitApp():
 root.destroy()
def cut():
 TextArea.event_generate(("<<Cut>>"))
def copy():
 TextArea.event_generate(("<<Copy>>"))
def paste():
 TextArea.event_generate(("<<Paste>>"))
def about():
 showinfo("NOTEPAD","Notpad by Nilesh Raj")
if __name__ =='__main__':
  root = Tk()
  root.title("untitled - Notpad")
 # root.wm_iconbitmap("1.ico")
  root.geometry("644x788")
 
  TextArea =Text(root,font="lucida 13")
  file =None
  TextArea.pack(expand=True,fill=BOTH)
  MenuBar = Menu(root)
  FileMenu =Menu(MenuBar,tearoff=0)
  FileMenu.add_command(label="New",command=newFile)
  FileMenu.add_command(label="open",command=openFile)
  FileMenu.add_command(label="Save",command=saveFile)
  FileMenu.add_separator()
  FileMenu.add_command(label="Exit",command=quitApp)
  MenuBar.add_cascade(label="file",menu=FileMenu)
 

  EditMenu =Menu(MenuBar,tearoff=0)
  EditMenu.add_command(label="cut",command=cut)
  EditMenu.add_command(label="copy",command=copy)
  EditMenu.add_command(label="paste",command=paste)
  MenuBar.add_cascade(label="Edit",menu=EditMenu)
 
  HelpMenu =Menu(MenuBar,tearoff=0)
  HelpMenu.add_command(label="About Notpad",command=about)
  MenuBar.add_cascade(label="Help",menu=HelpMenu)
 
  root.config(menu=MenuBar)
  Scroll = Scrollbar(TextArea)
  Scroll.pack(side=RIGHT,fill=Y)
  Scroll.config(command=TextArea.yview)
  TextArea.config(yscrollcommand=Scroll.set)
  root.mainloop()