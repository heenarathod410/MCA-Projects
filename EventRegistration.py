from tkinter import*
from tkinter import messagebox,ttk
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user = "root" , passwd = "root",database = "EventRegistration")
mycursor = mydb.cursor()

def clear():
    erid.delete(0,END)
    efname.delete(0,END)
    elname.delete(0,END)
    ephone.delete(0,END)
    ebranch.delete(0,END)
    eeventName.delete(0,END)
    erid.focus()

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    t6.set(item['values'][5])

def eventRegi():
    rid = t1.get()
    fnm = t2.get()
    lnm = t3.get()
    phn = t4.get()
    brc = t5.get()
    enm = t6.get()
    quary = "insert into tbl_eventRegistration values(%s,%s,%s, %s, %s,%s)"
    val = (rid,fnm,lnm,phn,brc,out)
    mycursor.execute(quary,val)
    mydb.commit()
    messagebox.showinfo("Information","Inserted successfully....")
    dispbtn()
    clear()
    return True

def cancleRagi():
    no = t1.get()
    if messagebox.askyesno("Confrim delete?","Are you sure to cancle ragistration?"):
        quary = "delete from tbl_eventRegistration where id = "+no
        mycursor.execute(quary)
        dispbtn()
        mydb.commit()
        clear()
    else:
        return True

def dispbtn():
    quary = "select id, fName, lName, phoneNo, branch, eventNam from tbl_eventRegistration"
    mycursor.execute(quary)
    disp = mycursor.fetchall()
    trv.delete(*trv.get_children())
    for i in disp:
        trv.insert("","end",values=i)

top = Tk()

wrp1 = LabelFrame(top,text="Details")
wrp2 = LabelFrame(top,text="data")

wrp1.pack(fill="both",expand="yes",padx=20,pady=10)
wrp2.pack(fill="both",expand="yes",padx=20,pady=10)

top.title("Event Registration")
top.geometry("1000x500")

t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()

rid = Label(wrp1,text="Enter ID:")
rid.grid(row=0, column=0, padx=5,pady=3,sticky='W')
erid = Entry(wrp1,textvariable=t1)
erid.grid(row=0, column=1, padx=5,pady=3,sticky='W')

fname = Label(wrp1,text="Enter First Name:")
fname.grid(row=1, column=0, padx=5,pady=3,sticky='W')
efname = Entry(wrp1,width=20,textvariable=t2)
efname.grid(row=1, column=1, padx=5,pady=3,sticky='W')

lname = Label(wrp1,text="Enter Last Name:")
lname.grid(row=2, column=0, padx=5,pady=3,sticky='W')
elname = Entry(wrp1,textvariable=t3)
elname.grid(row=2, column=1, padx=5,pady=3,sticky='W')

phone = Label(wrp1,text="Enter PhoneNo:")
phone.grid(row=3, column=0, padx=5,pady=3,sticky='W')
ephone = Entry(wrp1,textvariable=t4)
ephone.grid(row=3, column=1, padx=5,pady=3,sticky='W')

branch = Label(wrp1,text="Enter Branch:")
branch.grid(row=4, column=0, padx=5,pady=3,sticky='W')
ebranch = Entry(wrp1,textvariable=t5)
ebranch.grid(row=4, column=1, padx=5,pady=3,sticky='W')

eventName = Label(wrp1,text="Enter Event name:")
eventName.grid(row=5, column=0, padx=5,pady=3,sticky='W')
eeventName = Entry(wrp1,textvariable=t6)
eventList = ['Paper Presentation', 'Project Expo', 'Technical quiz', 'Spot event']
options = StringVar(top)
option = OptionMenu(wrp1,options,*eventList)
options.set('Select Events')
option.grid(row=5, column=1, padx=5,pady=3)
str_out = StringVar()
# str_out.set('Output')
def my_show(*args):
    return str_out.set(options.get())

out = my_show()
# options.trace_add('write',my_show)
# eeventName.grid(row=5, column=1, padx=5,pady=3)
# eeNam = Label(wrp1,text="Event name: ")
# eeNam.grid(row=5, column=2, padx=5,pady=3)


eventRBtn=Button(wrp1,text="Event Registration",command=eventRegi,bg='green',fg='white')
canRBtn=Button(wrp1,text="Cancel Registration",command=cancleRagi,bg='red',fg='white')
disBtn=Button(wrp1,text="Display",command=dispbtn,bg='blue',fg='white')

eventRBtn.grid(row=6, column=0, padx=5,pady=3)
canRBtn.grid(row=6, column=1, padx=5,pady=3)
disBtn.grid(row=6, column=2, padx=5,pady=3)

trv = ttk.Treeview(wrp2,columns=(1,2,3,4,5,6),show='headings',height="6",)
trv.pack(expand="yes")

trv.heading(1,text="ID")
trv.heading(2,text="First Name")
trv.heading(3,text="Last Name")
trv.heading(4,text="PhoneNo")
trv.heading(5,text="Branch")
trv.heading(6,text="Event name")

style = ttk.Style(top)
style.theme_use('clam')
#style.configure("Treeview",background="black",fieldbackground="black",foreground="white")
style.configure('Treeview.Heading',background="powderblue")

trv.bind('<Double 1>',getrow)

top.mainloop()
