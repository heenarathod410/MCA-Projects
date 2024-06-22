from tkinter import*
from tkinter import messagebox,ttk
import mysql.connector

def clear():
    esrno.delete(0,END)
    ename.delete(0,END)
    eadd.delete(0,END)
    esrno.focus()  


def addbtn():
    sno = esrno.get()
    nm = ename.get()
    ad = eadd.get()
    quary = "insert into tbl_addressBook values(%s,%s,%s)"
    val = (sno,nm,ad)
    mycursor.execute(quary,val)
    mydb.commit()
    messagebox.showinfo("Information","Inserted successfully....")
    dispbtn()
    clear()
    return True

def dispbtn():
    quary = "select Srno,Name,Address from tbl_addressBook"
    mycursor.execute(quary)
    disp = mycursor.fetchall()
    trv.delete(*trv.get_children())
    for i in disp:
        trv.insert("","end",values=i)
    

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])

def delbtn():
    no = t1.get()
    if messagebox.askyesno("Confrim delete?","Are you sure to delete this address?"):
        quary = "delete from tbl_addressBook where Srno = "+no
        mycursor.execute(quary)
        dispbtn()
        mydb.commit()
        clear()
    else:
        return True

def upbtn():
    sno = t1.get()
    uname = t2.get()
    uadd = t3.get()
    if messagebox.askyesno("confrim update?","Are you sure to update this address?"):
        quary = "update tbl_addressBook set  Name = %s , Address = %s where Srno = %s"
        val = (sno,uname,uadd)
        mycursor.execute(quary,val)
        dispbtn()
        mydb.commit()
    else:
        return True


mydb = mysql.connector.connect(host="localhost", user = "root" , passwd = "root",database = "addressbook")
mycursor = mydb.cursor()


top = Tk()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()

wrp1 = LabelFrame(top,text="Details")
wrp2 = LabelFrame(top,text="data")


wrp1.pack(fill="both",expand="yes",padx=20,pady=10)
wrp2.pack(fill="both",expand="yes",padx=20,pady=10)

top.title("Address Book")
top.geometry("800x500")

srno = Label(wrp1,text="Enter SRNO:")
srno.grid(row=0, column=0, padx=0,pady=3,sticky="W")
esrno = Entry(wrp1,textvariable=t1)
esrno.grid(row=0, column=1, padx=5,pady=3,columnspan=3,sticky="W")

name = Label(wrp1,text="Enter Name:")
name.grid(row=1, column=0, padx=0,pady=3,sticky="W")
ename = Entry(wrp1,width=20,textvariable=t2)
ename.grid(row=1, column=1, padx=5,pady=3,columnspan=3,sticky="W")

add = Label(wrp1,text="Enter Address:")
add.grid(row=2, column=0, padx=0,pady=3)
eadd = Entry(wrp1,width=40,textvariable=t3)
eadd.grid(row=2, column=1, padx=5,pady=3,columnspan=3)



trv = ttk.Treeview(wrp2,columns=(1,2,3),show='headings',height="6")
trv.pack(expand="yes")

trv.heading(1,text="SrNo")
trv.heading(2,text="Name")
trv.heading(3,text="Address")

style = ttk.Style(top)
style.theme_use('clam')
#style.configure("Treeview",background="black",fieldbackground="black",foreground="white")
style.configure('Treeview.Heading',background="powderblue")

trv.bind('<Double 1>',getrow)


AddBtn=Button(wrp1,text="Insert",command=addbtn,bg="green",fg="white")
modBtn=Button(wrp1,text="Modify",command=upbtn,bg="orange",fg="white")
disBtn=Button(wrp1,text="Display",command=dispbtn,bg="blue",fg="white")
delBtn=Button(wrp1,text="Delete",command=delbtn,bg="red",fg="white")

AddBtn.grid(row=4, column=0,padx=0,pady=3,sticky="W")
modBtn.grid(row=4, column=1,padx=0,pady=3,sticky="W")
disBtn.grid(row=4, column=2,padx=0,pady=3,sticky="W")
delBtn.grid(row=4, column=3,padx=0,pady=3,sticky="W")

top.mainloop()
