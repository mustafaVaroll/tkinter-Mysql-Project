from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="malatya44",
    database="veritabani"
)

cursor = con.cursor()

def insert():
    id = e_id.get()
    isim = e_isim.get()
    tel = e_tel.get()

    if(id=="" or isim=="" or tel==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        cursor.execute("insert into isci values('"+ id +"','"+ isim +"','"+ tel +"')")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_isim.delete(0, 'end')
        e_tel.delete(0, 'end')
        show()
        MessageBox.showinfo("Insert Status", "Inserted Succesfuly")
    

def delete():
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete Status", "Enter ID  for delete")
    else:
        
        cursor.execute("delete from isci where id='"+ e_id.get()+ "'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_isim.delete(0, 'end')
        e_tel.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete Status", "Deleted Succesfuly")
     

def update():
    id = e_id.get()
    isim = e_isim.get()
    tel = e_tel.get()

    if (id == "" or isim == "" or tel == ""):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        cursor.execute("update isci set isim='"+ isim +"', tel='"+ tel +"' where id='"+ id +"'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_isim.delete(0, 'end')
        e_tel.delete(0, 'end')
        show()
        MessageBox.showinfo("Update Status", "Updated Succesfuly")
       

def get():
    if (e_id.get() == ""):
        MessageBox.showinfo("Get Status", "Enter ID  for delete")
    else:
        cursor.execute("select * from isci where id='" + e_id.get() + "'")
        rows = cursor.fetchall()
        for row in rows:
            e_isim.insert(0, row[1])
            e_tel.insert(0,row[2])
      

def show():
    cursor.execute("select * from isci")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData = str(row[0])+ '   ' + str(row[1])+'   '+str(row[2])
        list.insert(list.size()+1, insertData)
    

root = Tk()
root.geometry("600x300")
root.title("Fİnal ")

id = Label(root, text='Enter ID', font=('bold', 10))
id.place(x=20, y=30)

isim = Label(root, text='Enter name', font=('bold', 10))
isim.place(x=20, y=60)

tel = Label(root, text='Enter phone', font=('bold', 10))
tel.place(x=20, y=90)

e_id = Entry()
e_id.place(x=150, y=30)

e_isim = Entry()
e_isim.place(x=150, y=60)

e_tel = Entry()
e_tel.place(x=150, y=90)

insert = Button(root, text="Insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root, text="Delete", font=("italic", 10), bg="white", command=delete)
delete.place(x=70, y=140)

update = Button(root, text="Update", font=("italic", 10), bg="white", command=update)
update.place(x=130, y=140)

get = Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=190, y=140)

list = Listbox(root)
list.place(x=290, y=30)
show()

root.mainloop()