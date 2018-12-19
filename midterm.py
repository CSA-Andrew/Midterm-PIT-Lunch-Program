#'''
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.
######
#Howard C Davis
#Final Tk
#'''

from tkinter import *
from tkinter import ttk
import math
def save(): #FILE/SAVE LOGGING ATTEMPT
    try:
        lfirst=list.curselection()
        file=open("lunch.txt", "a")
        file.write('\n')
        file.write(list.get(lfirst, None))
        file.write('\n')
        file.write(payment.get())
        file.write('\n')
        file.write(date.get())
        file.write('\n')
        file.write(employee.get())
        print("Pre")
        file.close()
        print("Closed")
        filewin = Toplevel(root)
        stuff = Label(filewin, text="Your lunch expense has been logged.")
        stuff.pack()
        button = Button(filewin, text="Close", command=filewin.destroy)
        button.pack()
        clear()
    except:
        errorfun()
def errorfun():
    error = Toplevel(root)
    msg = Label(error, text="There was an error with your entry,")
    msg.pack()
    msg2 = Label(error, text="please make sure to fill each box.")
    msg2.pack()
    bb1 = Button(error, text="Close", command=error.destroy)
    bb1.pack()
    clear()
def clear():
    pass
def checkout():
    try:
        total=0
        total=float(total)
        if var.get() == 1:
            total = total+1
        elif var.get() == 2:
            total = total+1
        elif var.get() == 3:
            total = total+.75
        elif var.get() == 4:
            total = total+1.25
        elif var.get() == 5:
            total = total+1
        lfirst = (list.curselection())
        meal = list.get(lfirst, None)
        crosscheck = "Sandwich[$3]", "Pizza [$4]", "Chicken Nuggets [$3.75]", "Chicken [$4]", "Tofu[$15]", "Gluten/Soy/Shellfish Free Clam Chowder [$20]"
        if meal == crosscheck[0]:
            total = total+3
        elif meal == crosscheck[1]:
            total = total+4
        elif meal == crosscheck[2]:
            total = total+3.75
        elif meal == crosscheck[3]:
            total = total+4
        elif meal == crosscheck[4]:
            total = total+15
        elif meal == crosscheck[5]:
            total = total+20
        print(meal)
        print(total)
        total=str(total)
        labeltotal.config(text="$" + total)

    except:
        pass
def add():
    progress["value"] = progress["value"] + 1
    progress.update()
def about(): #About page
    aboutb = Toplevel(root)
    description = Label(aboutb, text="This program is a quick lunch checkout")
    description.pack()
    desc1 = Label(aboutb, text="By Andrew Hilton, Adv. Comp. Prog. v.1")
    desc1.pack()
    bb = Button(aboutb, text="Close", command=aboutb.destroy)
    bb.pack()
def instructions():
    inst = Toplevel(root)
    desc = Label(inst, text="Input which items you'd like to have for lunch")
    desc2 = Label(inst, text=" aswell as your ID and payment method, then proceed to checkout!")
    desc.pack()
    desc2.pack()
    closeout = Button(inst, text="Close", command=inst.destroy)
    closeout.pack()
root = Tk()
menubar = Menu(root) #first menu defined, add all the parts
filemenu = Menu(menubar, tearoff=0) #says it is at the menubar, we have not defined yet
#add separator, usually to focus on something or to make it seem separate from other commands
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
#this actually adds the cascade, and you say what is in it. Think of it like a frame
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Instructions", command=instructions)
menubar.add_cascade(label="Help", menu=helpmenu)
var = IntVar()
D1 = Radiobutton(root, text="Soda [$1]", variable=var, value=1, anchor=W, command=add)
D1.grid(row=1, column=0, sticky=W)
D2 = Radiobutton(root, text="Tea [$1]", variable=var, value=2, anchor=W, command=add)
D2.grid(row=2, column=0, sticky=W)
D3 = Radiobutton(root, text="Milk [$.75]", variable=var, value=3, anchor=W, command=add)
D3.grid(row=3, column=0, sticky=W)
D4 = Radiobutton(root, text="Juice [$1.25]", variable=var, value=4, anchor=W, command=add)
D4.grid(row=4, column=0, sticky=W)
D5 = Radiobutton(root, text="Bottled Water [$1]", variable=var, value=5, anchor=W, command=add)
D5.grid(row=5, column=0, sticky=W)
lunches = ["Sandwich[$3]", "Pizza [$4]", "Chicken Nuggets [$3.75]", "Chicken [$4]", "Tofu[$15]", "Gluten/Soy/Shellfish Free Clam Chowder [$20]"]
items=StringVar(value=lunches)
list = Listbox(root, listvariable=items, width=45, height=6)
list.grid(row=0, column=0)
paymenttypes = ["Credit", "Cash", "Check"]
payment = ttk.Combobox(value=paymenttypes, state="readonly")
payment.grid(row=1, column=1, sticky=W)
days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
date=Spinbox(value=days, wrap=True, state="readonly")
date.grid(row=2, column=1, sticky=W)
eid=IntVar()
employee = Entry(textvariable=eid)
employee.grid(row=3, column=1, sticky=W)
progress= ttk.Progressbar(orient=HORIZONTAL, length=100, mode='determinate')
progress.grid(row=0, column=1, ipady=30, sticky=NSEW)
progress["maximum"] = 5
progress["value"] = 0
calc = Button(text="Calculate", command=checkout)
check = Button(text="Checkout", command=save)
calc.grid(row=4, column=1)
check.grid(row=5, column=1)
was = StringVar()
labeltotal = Label(textvariable="")
labeltotal.grid(row=6, column=1, sticky=S)
root.title("Pricing Calculator")
root.config(menu=menubar)
root.mainloop()