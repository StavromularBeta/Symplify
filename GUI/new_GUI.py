import Tkinter as tk


def runtext():
    print("This is the run text.")


def edittext():
    edit_text.set("This is the edit text.")

root = tk.Tk()

w = tk.Label(root,
             text="Symplify",
             padx=10,
             pady=10).pack()

frame = tk.Frame(root,
                 padx=10,
                 pady=10)
frame.pack()

quitbutton = tk.Button(frame,
                       text="Quit",
                       command=quit)

edit_text = tk.StringVar()
editbutton = tk.Button(frame,
                       textvariable=edit_text,
                       command=edittext)

edit_text.set("edit")

runbutton = tk.Button(frame,
                      text="Run",
                      command=runtext)

runbutton.pack()
editbutton.pack()
quitbutton.pack()

root.mainloop()

