from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="regi_form"
)
mycursor = mydb.cursor()

top = Tk()

top.geometry("900x900")

c = Canvas(top, bg="orange", height="800", width="800")

top.geometry("800x800")

name = Label(top, text="FIRST NAME",bg="orange",foreground="black").place(x=500, y=30)
name_loc = Label(top, text="(max 30 character a-z and A-Z)",bg="orange",foreground="black").place(x=750, y=30)

lname = Label(top, text="LAST NAME",bg="orange",foreground="black").place(x=500, y=60)
lname_loc = Label(top, text="(max 30 character a-z and A-Z)",bg="orange",foreground="black").place(x=750, y=60)

dob = Label(top, text="DATE OF BIRTH",bg="orange",foreground="black").place(x=500, y=90)

ttk.Label(top, text = "Month",).place(x=800,y=90)
n = tk.StringVar()
monthchoosen = ttk.Combobox(top, width = 10, textvariable = n)
monthchoosen['values'] = (' January',' February', ' March', ' April', ' May',' June',' July', ' August',' September',
' October',' November',' December')
monthchoosen.place(x=710, y=90)

ttk.Label(top, text="Date").place(x=670,y=90)
number = tk.StringVar()
numberChosen = ttk.Combobox(top, width=6, textvariable=number)
numberChosen['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
numberChosen.place(x=600, y=90)
numberChosen.current(0)
ttk.Label(top, text="Year").place(x=930,y=90)
number = tk.StringVar()
yearChosen = ttk.Combobox(top, width=6, textvariable=number)
yearChosen['values'] = (2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010)
yearChosen.place(x=860, y=90)

email = Label(top, text="EMAIL ID",bg="orange",foreground="black").place(x=500, y=120)
mobile = Label(top, text="MOBILE NO",bg="orange",foreground="black").place(x=500, y=150)
mobile_loc = Label(top, text="(max 10 digits only)" ,bg="orange",foreground="black").place(x=750, y=150)
gender = Label(top, text="GENDER" ,bg="orange",foreground="black").place(x=500, y=180)
addr = Label(top, text="ADDRESS" ,bg="orange",foreground="black").place(x=500, y=230)
city = Label(top, text="CITY" ,bg="orange",foreground="black").place(x=500, y=260)

pin = Label(top, text="PINCODE",bg="orange",foreground="black").place(x=500, y=290)
pin_loc = Label(top, text="(6 digit Number)",bg="orange",foreground="black").place(x=750, y=290)
state = Label(top, text="STATE",bg="orange",foreground="black").place(x=500, y=320)
country = Label(top, text="COUNTRY",bg="orange",foreground="black").place(x=500, y=350)
hobbies = Label(top, text="HOBBY",bg="orange",foreground="black").place(x=500, y=390)
edu = Label(top, text="EDUCATION",bg="orange",foreground="black").place(x=500, y=460)
sr = Label(top, text="SR",bg="orange",foreground="black").place(x=600, y=460)
ex = Label(top, text="EXAMINATION",bg="orange",foreground="black").place(x=650, y=460)
board = Label(top, text="BOARD",bg="orange",foreground="black").place(x=785, y=460)
board_loc = Label(top, text="(max 10 char)",bg="orange",foreground="black").place(x=770, y=600)

cs = Label(top, text="Courses \nApplied For",bg="orange",foreground="black").place(x=500, y=640)


per = Label(top, text="PERCENTAGE",bg="orange",foreground="black").place(x=900, y=460)
pet = Label(top, text="(upto 2 decimal)",bg="orange",foreground="black").place(x=900, y=600)

ep = Label(top, text="YEAR OF PASSING",bg="orange",foreground="black").place(x=1030, y=460)

one = Label(top, text="1",bg="orange",foreground="black").place(x=600, y=490)
two = Label(top, text="2",bg="orange",foreground="black").place(x=600, y=520)
three = Label(top, text="3",bg="orange",foreground="black").place(x=600, y=550)
four = Label(top, text="4",bg="orange",foreground="black").place(x=600, y=580)

ex1 = Label(top, text="Class X",bg="orange",foreground="black").place(x=670, y=490)
ex2 = Label(top, text="Class XII",bg="orange",foreground="black").place(x=670, y=520)
ex3 = Label(top, text="Diploma",bg="orange",foreground="black").place(x=670, y=550)
ex4 = Label(top, text="Degree",bg="orange",foreground="black").place(x=670, y=580)

# radio = IntVar()
#
# R1 = Radiobutton(top, text="Male",bg="orange",foreground="black", variable=radio,value=1)
# R1.pack(anchor=W)
# R1.place(x=600, y=180)
# R2 = Radiobutton(top, text="Female",bg="orange",foreground="black", variable=radio,value=2)
# R2.pack(anchor=W)
# R2.place(x=700, y=180)

radio = tk.StringVar()
radio.set("Male")

R1 = tk.Radiobutton(top, text="Male",bg="orange",foreground="black", variable=radio,value="Male")
R1.pack(anchor=W)
R1.place(x=600, y=180)
R2 = tk.Radiobutton(top, text="Female",bg="orange",foreground="black", variable=radio,value="Female")
R2.pack(anchor=W)
R2.place(x=700, y=180)

radio_2 = tk.StringVar()
radio_2.set("MCA")

R3 = tk.Radiobutton(top, text="MCA",bg="orange",foreground="black", variable=radio_2,value="MCA")
R3.pack(anchor=W)
R3.place(x=600, y=640)
R4 = tk.Radiobutton(top, text="M.COM",bg="orange",foreground="black", variable=radio_2,value="M.COM")
R4.pack(anchor=W)
R4.place(x=670, y=640)
R5 = tk.Radiobutton(top, text="MBA",bg="orange",foreground="black", variable=radio_2,value="MBA")
R5.pack(anchor=W)
R5.place(x=760, y=640)
R6 = tk.Radiobutton(top, text="M.SC",bg="orange",foreground="black", variable=radio_2,value="M.SC")
R6.pack(anchor=W)
R6.place(x=830, y=640)

checkvar1 = StringVar()
checkvar1.set("Drawing")
# checkvar2 = IntVar()
# checkvar3 = StringVar()
# checkvar4 = StringVar()
# checkvar5 = StringVar()

# chbtn = IntVar()
chkbtn1 = tk.Checkbutton(top, text="Drawing", bg="orange",variable = checkvar1 ,foreground="black",onvalue="Drawing",offvalue=0, height=1, width=10)
chkbtn1.pack()
chkbtn1.place(x=600, y=390)
chkbtn2 = tk.Checkbutton(top, text="Singing", bg="orange",variable = checkvar1 , foreground="black",  onvalue="Singing",offvalue=0, height=1, width=10)
chkbtn2.pack()
chkbtn2.place(x=680,y=390)
chkbtn3 = tk.Checkbutton(top, text="Dancing", bg="orange", variable = checkvar1 , foreground="black", onvalue="Dancing", offvalue=0, height=1, width=10)
chkbtn3.pack()
chkbtn3.place(x=770,y=390)
chkbtn4 = tk.Checkbutton(top, text="Sketching", bg="orange", variable =checkvar1 , foreground="black",onvalue="Sketching", offvalue=0, height=1, width=10)
chkbtn4.pack()
chkbtn4.place(x=850,y=390)
chkbtn5 = tk.Checkbutton(top, text="Sports", bg="orange", variable = checkvar1 , foreground="black", onvalue="Sports", offvalue=0, height=1, width=10)
chkbtn5.pack()
chkbtn5.place(x=595,y=420)

e1 = Entry(top)
e1.place(x=600, y=30)
e2 = Entry(top)
e2.place(x=600, y=60)
e3 = Entry(top)
e3.place(x=600, y=120)
e4 = Entry(top)
e4.place(x=600, y=150)
e5 = Entry(top)
e5.place(x=600, y=230)
e6 = Entry(top)
e6.place(x=600, y=260)
e7 = Entry(top)
e7.place(x=600, y=290)
e8 = Entry(top)
e8.place(x=600, y=320)
e9 = Entry(top)
e9.place(x=600, y=350)
# e10 = Entry(top)
# e10.place(x=700, y=420)
e11 = Entry(top)
e11.place(x=750, y=490)
e12 = Entry(top)
e12.place(x=750, y=520)
e13 = Entry(top)
e13.place(x=750, y=550)
e14 = Entry(top)
e14.place(x=750, y=580)
e15 = Entry(top)
e15.place(x=885, y=490)
e16 = Entry(top)
e16.place(x=885, y=520)
e17 = Entry(top)
e17.place(x=885, y=550)
e18 = Entry(top)
e18.place(x=885, y=580)
e19 = Entry(top)
e19.place(x=1020, y=490)
e20 = Entry(top)
e20.place(x=1020, y=520)
e21 = Entry(top)
e21.place(x=1020, y=550)
e22 = Entry(top)
e22.place(x=1020, y=580)

def fun2():
    name = e1.get()
    print(name)
    lname = e2.get()
    print(lname)
    n = monthchoosen.get()
    print(n)
    number = numberChosen.get()
    print(number)
    year = yearChosen.get()
    print(year)
    email = e3.get()
    print(email)
    mobile = e4.get()
    print(mobile)
    gender = radio.get()
    print(gender)
    addr = e5.get()
    print(addr)
    city = e6.get()
    print(city)
    pin = e7.get()
    print(pin)
    state = e8.get()
    print(state)
    country = e9.get()
    print(country)
    hobbies = StringVar.get(checkvar1)
    # hobbies = IntVar.get(checkvar2)
    # hobbies = StringVar.get(checkvar3)
    # hobbies = StringVar.get(checkvar4)
    # hobbies = StringVar.get(checkvar5)
    # chk = IntVar.get(checkvar1)
    # hobbies = e10.get()
    # print(hobbies)
    board_X = e11.get()
    board_XII = e12.get()
    board_Dip = e13.get()
    board_Deg = e14.get()
    per_X = e15.get()
    per_XII = e16.get()
    per_Dip = e17.get()
    per_Deg = e18.get()
    ep_X = e19.get()
    ep_XII = e20.get()
    ep_Dip = e21.get()
    ep_Deg = e22.get()
    cource_applied = radio_2.get()
    print(cource_applied)

    mycursor = mydb.cursor()
    sql = "INSERT INTO form_data (Fname,Lname,Day,Month,Year,Email,Mobile,Gender,Address,City,Pin,State,Country,Hobby,Class_X_Board,Class_X_Percentage,Class_X_Year_Of_Passing,Class_XII_Board,Class_XII_Percentage,Class_XII_Year_Of_Passing,Diploma_Board,Diploma_Percentage,Diploma_Year_Of_Passing,Degree_Board,Degree_Percentage,Degree_Year_Of_Passing,Cource_Applied) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
    val = (name,lname,number,n,year,email,mobile,gender,addr,city,pin,state,country,hobbies,board_X,per_X,ep_X,board_XII,per_XII,ep_XII,board_Dip,per_Dip,ep_Dip,board_Deg,per_Deg,ep_Deg,cource_applied)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("Hello", "Do You Want To Submit")
    x = messagebox.askquestion('Yes|No', 'Do you want to Exit?')
    if x == "no":
        # top.destroy()
        quit()
    else:
        fun1()
    # messagebox.showinfo("Hello", "Do You Want To Submit")
def fun1():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e15.delete(0, END)
    e16.delete(0, END)
    e17.delete(0, END)
    e18.delete(0, END)
    e19.delete(0, END)
    e20.delete(0, END)
    e21.delete(0, END)
    e22.delete(0, END)
    monthchoosen.delete(0, END)
    yearChosen.delete(0 ,END)
    numberChosen.delete(0, END)
    # messagebox.showinfo("Hello", "Do You Want To Reset")
def reset_fun():
    messagebox.showinfo("Hello", "Do You Want To Reset")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e15.delete(0, END)
    e16.delete(0, END)
    e17.delete(0, END)
    e18.delete(0, END)
    e19.delete(0, END)
    e20.delete(0, END)
    e21.delete(0, END)
    e22.delete(0, END)
    monthchoosen.delete(0, END)
    yearChosen.delete(0 ,END)
    numberChosen.delete(0, END)

sbmitbtn = Button(top, text = "Submit",command = fun2,activebackground = "orange", activeforeground = "blue").place(x = 680, y = 700)
sbmitbtn_2 = Button(top, text = "Reset",command=reset_fun,activebackground = "orange", activeforeground = "blue").place(x = 780, y = 700)


c.pack()
top.mainloop()