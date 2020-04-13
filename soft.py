from tkinter import Tk, Button,Label,Scrollbar,Listbox,StringVar,Entry,W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox


root = Tk()  # Creates application window

root.title("Database Application") # Adds a title to application window
root.configure(background="light green")  # Add background color to application window
root.geometry("850x500")  # Sets a size for application window
root.resizable(width=False,height=False) # Prevents the application window from resizing

# Create Labels and entry widgets

imone_label =ttk.Label(root,text="Įmonė",background="light green",font=("TkDefaultFont", 16))
imone_label.grid(row=0, column=0, sticky=W)
imone_text = StringVar()
imone_entry = ttk.Entry(root,width=24,textvariable=imone_text)
imone_entry.grid(row=0, column=1, sticky=W)

sf_numeris_label =ttk.Label(root,text="S/F numeris",background="light green",font=("TkDefaultFont", 16))
sf_numeris_label.grid(row=0, column=2, sticky=W)
sf_numeris_text = StringVar()
sf_numeris_entry = ttk.Entry(root,width=24,textvariable=sf_numeris_text)
sf_numeris_entry.grid(row=0, column=3, sticky=W)

data_label =ttk.Label(root,text="data",background="light green",font=("TkDefaultFont", 14))
data_label.grid(row=0, column=4, sticky=W)
data_text = StringVar()
data_entry = ttk.Entry(root,width=24,textvariable=data_text)
data_entry.grid(row=0, column=5, sticky=W)

root.mainloop()  # Runs the application until exit