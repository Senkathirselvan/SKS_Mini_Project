from tkinter import*
from tkinter import messagebox
import mysql.connector

trial_time=0
def login_time():
    global trial_time

    trial_time+=1
    if trial_time==3:
        messagebox.showwarning("Warning","You have tried more then the limit!!!")
        root.destroy()

def loginuser():
    username=user.get()
    password=code.get()
    print(username,password)
    if (username=="" or username=="UserID") or (password=="" or  password=="Password"):
        messagebox.showerror("Entry error","Type User name or Password!!")
    else:
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="senkathir420@",database="SKS_login")
            mycursor=mydb.cursor()
            print("connected to the database!!!")
        except:
            messagebox.showerror("Connection","Database connection not stablish!!") 
            return
        
        command="use SKS_login"
        mycursor.execute(command)

        command="select * from user_details where User_NAME=%s and Password=%s"
        mycursor.execute(command,(username,password))
        myresult=mycursor.fetchone()
        print(myresult)

        if myresult==None:
            messagebox.showinfo("invalid","invalid userid and password")
            login_time()

        else: 
            messagebox.showinfo("Login","login sucesfully")

def loginuser():
    root.destroy()
    import main

def createuser():
    root.destroy()
    import create_account
            

root=Tk()
root.title("LOGIN PAGE")
root.geometry("1300x715")
root.resizable(False,False)

# Icon image:
icon_image=PhotoImage(file="/home/senkathir/Desktop/SKS/images/images (5).png")
root.iconphoto(False,icon_image)

# Background Image:
bgimage=PhotoImage(file="/home/senkathir/Desktop/SKS/images/login(1300x715).png")
Label(root,image=bgimage).pack()

# User Entry:
def user_enter(event):
    user.delete(0,"end")

def user_leave(event):
    name=user.get()
    if name=="":
        user.insert(0,"UserID")

user=Entry(root,width=22,bg="white",fg="black",font=("Arial Bold",19))
user.place(x=517,y=248)
user.insert(0,"User ID")
user.bind("<FocusIn>",user_enter)
user.bind("<FocusOut>",user_leave)

# Password Entry:
def password_enter(event):
    code.delete(0,'end')
def password_leave(event):
    pasword=code.get()
    if pasword=='':
        code.insert(0,"Password")
code=Entry(root,width=22,fg="black",bg="white",font=("Arial Bold",19))
code.place(x=517,y=335)
code.insert(0,"Password")
code.bind("<FocusIn>",password_enter)
code.bind("<FocusOut>",password_leave)

# Open eye image:
button_mode=True

def hide():
    global button_mode

    if button_mode:
        eyebutton.config(image=closeeye,activebackground="white")
        code.config(show="*")
        button_mode=False
    else:
        eyebutton.config(image=openeye,activebackground="white")
        code.config(show="")
        button_mode=True

closeeye=PhotoImage(file="/home/senkathir/Desktop/SKS/images/pngwing.com (9).png")
openeye=PhotoImage(file="/home/senkathir/Desktop/SKS/images/pngwing.com (10).png")
eyebutton=Button(root,image=closeeye,bg="white",bd=0,command=hide)
eyebutton.place(x=800,y=345)

login_Button=Button(text="LOGIN",width=14,bg="black",bd=-15,fg="white",font=('Arial Bold',14),command=loginuser)
login_Button.place(x=586,y=413)

create1_Button=Button(text="CREATE",width=6,bg="black",bd=-15,fg="white",font=('Arial Bold',13),command=createuser)
create1_Button.place(x=1211,y=65)

root.mainloop()
