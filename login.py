from tkinter import *
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")

        F1=Frame(self.root,bd=10,relief=GROOVE)
        F1.place(x=400,y=150,height=350)
#variables===========
        self.user=StringVar()
        self.password=StringVar()


        title=Label(F1,text="LOGIN SYSTEM",font=("times new roman",35,"bold")).grid(row=0,columnspan=2,pady=30)
#Username==============
        lblusername=Label(F1,text="Username",font=("times new roman",25,"bold")).grid(row=1,column=0,padx=10,pady=10)
        txtuser=Entry(F1,bd=7,relief=GROOVE,textvariable=self.user,width=25,font=("arial 15 bold")).grid(row=1,column=1,padx=10,pady=10)
#password==============
        lblpass=Label(F1,text="Password",font=("times new roman",25,"bold")).grid(row=2,column=0,padx=10,pady=10)
        txtpass=Entry(F1,bd=7,relief=GROOVE,show="*",textvariable=self.password,width=25,font=("arial 15 bold")).grid(row=2,column=1,padx=10,pady=10)

#Button================
        btnlog=Button(F1,text="Login",font=("arial 15 bold"),bd=7,width=10,command=self.logfun).place(x=10,y=260)
        btnreset=Button(F1,text="Reset",font=("arial 15 bold"),bd=7,width=10,command=self.reset).place(x=162,y=260)
        btnexit=Button(F1,text="Exit",font=("arial 15 bold"),bd=7,width=10,command=self.exit_fun).place(x=312,y=260)

  
    def logfun(self):
        if self.user.get()=="Akash" and self.password.get()=="123456":
            messagebox.showinfo("Info",f"Welcome! {self.user.get()} and your password is :{self.password.get()}")
            self.root.destroy()
            import software
            software.File_App()
        else:
            messagebox.showerror("Error","Invalid Username or Password")
        
    def reset(self):
        self.user.set("")
        self.password.set("")

    def exit_fun(self):
        option=messagebox.askyesno("Exit","Do You really want to exit?")
        if option>0:
            self.root.destroy()
        else:
            return


root=Tk()
ob=Login(root)
root.mainloop()