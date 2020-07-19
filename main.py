from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
from tkinter import Text
from tkinter import filedialog

#Functions

def save():
    if os.path.isfile("save/"+title.get()+".txt"):
        messagebox.showerror("Failed!", "File already exist!")
    else:
        print("t")
        save = open("save/" + title.get() + ".txt", "a+")
        save.write(writing_space.get("1.0", "end-1c"))
        writing_space.delete(1.0, END)
        title.delete(0, END)
        messagebox.showinfo("Success", "File Saved!")
        save.close()
def new_file():
    responde = messagebox.askyesnocancel(title= "New File", message = "Do You want to save?")
    if responde == True:
        if os.path.isfile("save/" + title.get() + ".txt"):
            overwrite = messagebox.askyesno(title = "Warning", message ="File already exist, do you want to overwrite it?")
            if overwrite == True:
                save = open("save/" + title.get() + ".txt", "a+")
                save.write(writing_space.get("1.0", "end-1c"))
                writing_space.delete(1.0, END)
                title.delete(0, END)
                messagebox.showinfo("Success", "File Saved!")
                save.close()
            else:
                return
        else:
            save = open("save/" + title.get() + ".txt", "a+")
            save.write(writing_space.get("1.0", "end-1c"))
            writing_space.delete(1.0, END)
            title.delete(0, END)
            messagebox.showinfo("Success", "File Saved!")
            save.close()
    elif responde == False:
        writing_space.delete(1.0, END)
        title.delete(0, END)
    else:
        return

def otworz():
        root.filename = filedialog.askopenfilename(initialdir="notepad/save", title="Choose file",filetypes = (("txt files", "*.txt"),("all files", "*.*")))
        r = open(root.filename, "r")
        writing_space.delete(1.0, END)
        writing_space.insert(1.0, r.read())



root = Tk()
root.iconbitmap("icons/feather_quill_pen_write_sign_icon_124655.ico")
root.title("Notepad")
root.geometry("1920x1080")



#Frames
frame1 = LabelFrame(root, text = "Your Files")
frame1.grid(row = 2, column = 0, sticky = N)

#Buttons
new_file = Button(root, text = "New File", command =new_file)
new_file.grid(row = 0, column = 2)

save = Button(root, text = "Save", command = save)
save.grid(row = 0, column = 3)

otworz = Button(root, text = "Open", command = otworz)
otworz.grid(row =0, column = 4)

#Writing space
name = Label(root, text = "Name of file")
name.grid(row = 0, column = 0)
title = Entry(root)
title.grid(row = 0, column = 1)

writing_space = Text(root, width = 100, height = 1079)
writing_space.grid(row = 2, column = 1, columnspan = 122, padx =2)

#Your files
for file in os.listdir("save/"):
    file_name = Label(frame1, text = file).pack(anchor = N)

root.mainloop()