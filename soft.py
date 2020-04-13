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

# Add a button to insert inputs into database

add_btn = Button(root, text="Add Book",bg="blue",fg="white",font="helvetica 10 bold",command=add_book)
add_btn.grid(row=0, column=6, sticky=W)

# Add  a listbox  to display data from database
list_bx = Listbox(root,height=16,width=40,font="helvetica 13",bg="light blue")
list_bx.grid(row=3,column=1, columnspan=14,sticky=W + E,pady=40,padx=15)
list_bx.bind('<<ListboxSelect>>',get_selected_row)

# Add scrollbar to enable scrolling
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1,column=8, rowspan=14,sticky=W )

list_bx.configure(yscrollcommand=scroll_bar.set) # Enables vetical scrolling
scroll_bar.configure(command=list_bx.yview)

# Add more Button Widgets

modify_btn = Button(root, text="Modify Record",bg="purple",fg="white",font="helvetica 10 bold",command=update_records)
modify_btn.grid(row=15, column=4)

delete_btn = Button(root, text="Delete Record",bg="red",fg="white",font="helvetica 10 bold",command=delete_records)
delete_btn.grid(row=15, column=5)

view_btn = Button(root, text="View all records",bg="black",fg="white",font="helvetica 10 bold",command=view_records)
view_btn.grid(row=15, column=1)#, sticky=tk.N)

clear_btn = Button(root, text="Clear Screen",bg="maroon",fg="white",font="helvetica 10 bold",command=clear_screen)
clear_btn.grid(row=15, column=2)#, sticky=tk.W)

exit_btn = Button(root, text="Exit  Application",bg="blue",fg="white",font="helvetica 10 bold",command=root.destroy)
exit_btn.grid(row=15, column=3)



root.mainloop()  # Runs the application until exit