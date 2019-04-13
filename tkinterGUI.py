from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("700x500")
scheduledimage=PhotoImage("...")
note = ttk.Notebook(root)

tab1 = ttk.Frame(note)
tab2 = ttk.Frame(note)
tab3 = ttk.Frame(note)

text = Label(tab1, text="This is Cornell Cup.", width=50)
text.pack(side=LEFT)

note.add(tab1, text = "Tab One")
note.add(tab2, text = "Tab Two")
note.add(tab3, text = "Tab Three")
note.pack()

root.mainloop()