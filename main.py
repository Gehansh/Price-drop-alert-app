from tkinter import *
from tkinter import messagebox as mbx
from tracker import check_price

root = Tk()

icon=PhotoImage(file="C:/Users/Lenovo/Pictures/drop.png")
root.iconphoto(root,icon)
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
w = 700
h = 300
x = (x - w) // 2
y = (y - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")
root.title("Price Drop Alert App")
res = StringVar()
strobj=StringVar()
strobj.set("Enter above Details..")

def setfn():
    res_label.config(fg="green")
    strobj.set("You will Recieve our mail as soon as "+name_entry.get()+" Price Drops!!")
    url_name=url_entry.get()
    mail_name=mail_entry.get()
    pref_prize=prize_entry.get()
    check_price(url_name,mail_name,pref_prize)


def clearfn():
    url_entry.delete(0, END)
    mail_entry.delete(0, END)
    prize_entry.delete(0, END)
    res_label.config(fg="black")
    strobj.set("Enter above Details..")
    url_entry.focus()


def quitfn():
    response = mbx.askyesno("Confirm Exit", "Are you sure you want to exit?")
    if response:
        root.destroy()


header = Label(root, text="Price Drop Alert App", font="Arial 20 bold")
name_label = Label(root, text="Enter Product Name :",width=str(int(w/20)))
url_label = Label(root, text="Enter Product URL :",width=str(int(w/20)))
mail_label = Label(root, text="Enter your mail id :",width=str(int(w/20)))
prize_label = Label(root, text="Min Expected Price :",width=str(int(w/20)))

name_entry = Entry(root,width=str(int(w/15)))
url_entry = Entry(root,width=str(int(w/15)))
mail_entry = Entry(root, width=str(int(w/15)))
prize_entry = Entry(root, width=str(int(w/15)))

res_label = Label(root, textvariable=strobj)

set = Button(root, text="Set", command=setfn)
clear = Button(root, text="Clear", command=clearfn)
quit = Button(root, text="Quit", command=quitfn)

header.grid(row="0", column="0", columnspan="3",pady="20")

name_label.grid(row="1", column="0", sticky=E)
name_entry.grid(row="1", column="1")

url_label.grid(row="2", column="0", sticky=E)
url_entry.grid(row="2", column="1")

mail_label.grid(row="3", column="0", sticky=E)
mail_entry.grid(row="3", column="1")

prize_label.grid(row="4", column="0", sticky=E)
prize_entry.grid(row="4", column="1")

res_label.grid(row="5", column="0",columnspan="3",pady="20")

set.grid(row="6", column="0", sticky=W + E, padx="25", pady="15")
clear.grid(row="6", column="1", sticky=W + E, padx="5", pady="15")
quit.grid(row="6", column="2", sticky=W + E, padx="5", pady="15")

root.mainloop()
