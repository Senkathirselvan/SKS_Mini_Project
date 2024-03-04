from tkinter import*
from tkinter import messagebox
import mysql.connector

# Create New User Account:
def create():
    adminpassword=Ad_password.get()
    username=User_Name_entry.get()
    password=password_entry.get()
    print(adminpassword,username, password)

    if adminpassword=="senkathir420@":  
        if (username == "User NAME" or username == "") or (password == "Password" or password == ""):
            messagebox.showerror("Entry error", "Type User Name or Password!!")



        else:
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",password="senkathir420@",database="SKS_login")
                mycursor=mydb.cursor()
                print("connected to the database!!!")
            except:
                messagebox.showinfo("Connection","Database Connection not Stablish!!") 

            try:
                command="create database SKS_login"
                mycursor.execute(command)

                command="use  SKS_login"
                mycursor.execute(command)

                command="create table user_details(user int auto_increment key not null,user_NAME varchar(50) not null,password varchar(50) not null)"
                mycursor.execute(command)

            except:
                mycursor.execute("use SKS_login")
                mydb=mysql.connector.connect(host="localhost",user="root",password="senkathir420@",database="SKS_login")
                mycursor=mydb.cursor()

                command="insert into user_details(User_NAME,Password) values(%s,%s)"
                mycursor.execute(command,(username,password))
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Create","New User Add Successfully!!") 
    else:
        messagebox.showerror("Admin Password","Please Type Correct Admin Password!!") 

# Login Destroy:
def login():
    root.destroy()
    import SKS


root=Tk()
root.title("CREAT NEW ACCOUNT")
root.geometry("1300x715")
root.resizable(False,False)


# Icon image:
icon=PhotoImage(file="/home/senkathir/Desktop/SKS/images/images (4).png")
root.iconphoto(False,icon)

# Background image:
bg_image=PhotoImage(file="/home/senkathir/Desktop/SKS/images/create(1300x715).png")
Label(root,image=bg_image).pack()

# Admin Password Entry:
def Ad_password_enter(event):
    Ad_password.delete(0,"end")

def Ad_password_leave(event):
    name=Ad_password.get()
    if name=="":
       Ad_password.insert(0,"ADMINPASSWORD")

Ad_password=Entry(root,width=19,bg="white",fg="black",font=("Arial Bold",19),show="*")
Ad_password.place(x=515,y=233)
Ad_password.insert(0,"ADMINPASSWORD")
Ad_password.bind("<FocusIn>",Ad_password_enter)
Ad_password.bind("<FocusOut>",Ad_password_leave)

# User Name Entry:
def User_Name_enter(event):
    User_Name_entry.delete(0,"end")

def User_Name_leave(event):
    name=User_Name_entry.get()
    if name=="":
        User_Name_entry.insert(0,"User NAME")
       
User_Name_entry=Entry(root,width=19,bg="white",fg="black",font=("Arial Bold",19))
User_Name_entry.place(x=515,y=309)
User_Name_entry.insert(0,"User NAME")
User_Name_entry.bind("<FocusIn>",User_Name_enter)
User_Name_entry.bind("<FocusOut>",User_Name_leave)

# Password Entry:
def password_enter(event):
    password_entry.delete(0,"end")

def password_leave(event):
    conform=password_entry.get()
    if conform=="":
        password_entry.insert(0,"Password")

password_entry=Entry(root,width=19,bg="white",fg="black",font=("Arial Bold",19))
password_entry.place(x=515,y=387)
password_entry.insert(0,"Password")
password_entry.bind("<FocusIn>",password_enter)
password_entry.bind("<FocusOut>",password_leave)

# Button:
create2_button=Button(text="CREATE",width=11,bd=0,fg="white",bg="black",font=("Arial Bold",18),command=create)
create2_button.place(x=563,y=470)

back_button=Button(text="BACK",width=6,bg="black",bd=-15,fg="white",font=('Arial Bold',13),command=login)
back_button.place(x=1,y=66)

root.mainloop()