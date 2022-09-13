from tkinter import *

# initialize window
root = Tk()
root.geometry('500x500')
root.config(bg='BLACK')
root.title('Code Warraor')
root.resizable(0, 0)
contactlist = [
    ['Parvez Ahmed', '01307864301', 'parvez15-13438@diu.edu.bd'],
    ['Amit Barai', '01999309779', 'amit-15-13513@diu.edu.bd'],
    ['Nusrath Jahan Nishu', '01842717991', 'nusrath15-13574@diu.edu.bd'],
    ['Sukanta Paul', '01301648901', 'sukanta.p29@gmail.com'],
    ['Sadman Sadik', '01952034689', 'sadman94@gmail.com'],
    ['Alvi Rahman', '01853649720', 'alvi.r165@gmail.com'],
]

Name = StringVar()
Number = StringVar()
Email = StringVar()

# create frame
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL,)
select = Listbox(frame, yscrollcommand=scroll.set, height=12, bg='SlateGray3')
scroll.config(command=select.yview,)
scroll.pack(side=RIGHT, fill=Y,)
select.pack(side=LEFT, fill=BOTH, expand=1)


########### function to get select value

def Selected():
    return int(select.curselection()[0])


##fun to add new contact
def AddContact():
    contactlist.append([Name.get(), Number.get(), Email.get()])
    Select_set()


# fun to edit existing contact(first select the contact then click on view button then edit the contact and then click on edit button)
def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get(), Email.get()]
    Select_set()


# to delete selected contact
def DELETE():
    del contactlist[Selected()]
    Select_set()


# to view selected contact(first select then click on view button)
def VIEW():
    NAME, PHONE, MAIL = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Email.set(MAIL)

def SEARCH():
    NAME, PHONE, MAIL = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Email.set(MAIL)

###exit game window
def EXIT():
    root.destroy()


# empty name and number field
def RESET():
    Name.set('')
    Number.set('')
    Email.set('')


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone, mail in contactlist:
        select.insert(END, name)


Select_set()

######define buttons #####labels and entry widget
Label(root, text='NAME', font='arial 12 bold', bg='SlateGray3').place(x=30, y=15)
Entry(root, textvariable=Name).place(x=90, y=20)
Label(root, text='PHONE NO.', font='arial 12 bold', bg='SlateGray3').place(x=30, y=60)
Entry(root, textvariable=Number).place(x=130, y=65)
Label(root, text='E-MAIL: ', font='arial 12 bold', bg='SlateGray3').place(x=30, y=105)
Entry(root, textvariable=Email).place(x=110, y=110)


Button(root, text=" ADD", font='arial 12 bold', bg='SlateGray4', command=AddContact).place(x=30, y=160)
Button(root, text="EDIT", font='arial 12 bold', bg='SlateGray4', command=EDIT).place(x=30, y=310)
Button(root, text="DELETE", font='arial 12 bold', bg='SlateGray4', command=DELETE).place(x=30, y=360)
Button(root, text="VIEW", font='arial 12 bold', bg='SlateGray4', command=VIEW).place(x=30, y=160+50)
Button(root, text="SEARCH", font='arial 12 bold', bg='SlateGray4', command=SEARCH).place(x=30, y=260)
Button(root, text="EXIT", font='arial 12 bold', bg='PINK', command=EXIT).place(x=240, y=440)
Button(root, text="RESET", font='arial 12 bold', bg='SlateGray4', command=RESET).place(x=30, y=410)

root.mainloop()