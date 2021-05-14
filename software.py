from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
class File_App:
    def __init__(self):
        self.root=Tk()
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="FILE BASED RECORD SYSTEM",bd=10,relief=GROOVE,pady=10,font=("times new roman",30,"bold")).pack(fill=X)

        Student_Frame=Label(self.root,bd=10,relief=GROOVE)
        Student_Frame.place(x=20,y=100,width=1025,height=450)

        stitle=Label(Student_Frame,text="STUDENT DETAILS",font=("times new roman",25,"bold")).grid(row=0,columnspan=4,pady=20,sticky="w")

#All Variables===============
        self.s_id=StringVar()
        self.name=StringVar()
        self.course=StringVar()
        self.address=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.degree=StringVar()
        self.proof=StringVar()
        self.payment=StringVar()


#id==================
        lblsid=Label(Student_Frame,text="Student ID",font=("times new roman",20,"bold")).grid(row=1,column=0,pady=10,padx=10,sticky="w")
        txtsid=Entry(Student_Frame,textvariable=self.s_id,bd=7,relief=GROOVE,font=("times new roman",20,"bold"),width=20).grid(row=1,column=1,pady=10,padx=10)
#name-==============
        lblname=Label(Student_Frame,text="Name",font=("times new roman",20,"bold")).grid(row=2,column=0,pady=10,padx=10,sticky="w")
        txtname=Entry(Student_Frame,textvariable=self.name,bd=7,relief=GROOVE,font=("times new roman",20,"bold"),width=20).grid(row=2,column=1,pady=10,padx=10)
#course=============
        lblcourse=Label(Student_Frame,text="Course",font=("times new roman",20,"bold")).grid(row=3,column=0,pady=10,padx=10,sticky="w")
        txtcourse=Entry(Student_Frame,textvariable=self.course,bd=7,relief=GROOVE,font=("times new roman",20,"bold"),width=20).grid(row=3,column=1,pady=10,padx=10)
#Address============
        lbladdress=Label(Student_Frame,text="Address",font=("times new roman",20,"bold")).grid(row=4,column=0,pady=10,padx=10,sticky="w")
        txtaddress=Entry(Student_Frame,textvariable=self.address,bd=7,relief=GROOVE,font=("times new roman",20,"bold"),width=20).grid(row=4,column=1,pady=10,padx=10)

#City==============
        lblcity=Label(Student_Frame,text="City",font=("times new roman",20,"bold")).grid(row=5,column=0,pady=10,padx=10,sticky="w")
        txtcity=Entry(Student_Frame,textvariable=self.city,bd=7,relief=GROOVE,font=("times new roman",20,"bold"),width=20).grid(row=5,column=1,pady=10,padx=10)

############################################################################################################

#Contact No===========
        lblcontact=Label(Student_Frame,text="Contact No",font=("times new roman",20,"bold")).grid(row=1,column=2,pady=10,padx=10,sticky="w")
        txtcontact=Entry(Student_Frame,textvariable=self.contact,bd=7,relief=GROOVE,font=("times new roman",20,"bold"),width=20).grid(row=1,column=3,pady=10,padx=10)
#Date()dd/mm/yy========
        lbldate=Label(Student_Frame,text="Date(dd/mm/yy)",font=("times new roman",20,"bold")).grid(row=2,column=2,pady=10,padx=10,sticky="w")
        txtcontact=Entry(Student_Frame,textvariable=self.date,bd=7,relief=GROOVE,font=("times new roman",20,"bold"),width=20).grid(row=2,column=3,pady=10,padx=10)
#Select Degree==========
        lbDegree=Label(Student_Frame,text="Select Degree",font=("times new roman",20,"bold")).grid(row=3,column=2,pady=10,padx=10,sticky="w")
        degreecombo=ttk.Combobox(Student_Frame,textvariable=self.degree,width=20,state="readonly",font="arial 17 bold")
        degreecombo['values']=('BCA','MCA','Bsc','Msc','BTech','MTech')
        degreecombo.grid(row=3,column=3,pady=10,padx=10)
#ID Proof=============
        lblproof=Label(Student_Frame,text="ID Proof",font=("times new roman",20,"bold")).grid(row=4,column=2,pady=10,padx=10,sticky="w")
        proofcombo=ttk.Combobox(Student_Frame,textvariable=self.proof,width=20,state="readonly",font="arial 17 bold")
        proofcombo['values']=('Aadhar Card','Driving Lic','Voter Card','Pan Card','Electricity Bill','Family Cert')
        proofcombo.grid(row=4,column=3,pady=10,padx=10)
#Payment mode===========
        lblpayment=Label(Student_Frame,text="Payment Mode",font=("times new roman",20,"bold")).grid(row=5,column=2,pady=10,padx=10,sticky="w")
        paymentcombo=ttk.Combobox(Student_Frame,textvariable=self.payment,width=20,state="readonly",font="arial 17 bold")
        paymentcombo['values']=('Debit Card','Credit Card','UPI','Wallet','Cash','Pay Later')
        paymentcombo.grid(row=5,column=3,pady=10,padx=10)




#==================Button=====================
        btnFrame=Frame(self.root,bd=10,relief=GROOVE)
        btnFrame.place(x=20,y=570,width=1320,height=120)

        btnsave=Button(btnFrame,text="Save",font="arial 15 bold",bd=7,width=16,command=self.save_data).grid(row=0,column=0,padx=20,pady=20)
        btndelete=Button(btnFrame,text="Delete",font="arial 15 bold",bd=7,width=16,command=self.delete).grid(row=0,column=1,padx=20,pady=20)
        btnclear=Button(btnFrame,text="Clear",font="arial 15 bold",bd=7,width=16,command=self.clear).grid(row=0,column=2,padx=20,pady=20)
        btnslog=Button(btnFrame,text="Logout",font="arial 15 bold",bd=7,width=16,command=self.logout).grid(row=0,column=3,padx=20,pady=20)
        btnexit=Button(btnFrame,text="Exit",font="arial 15 bold",bd=7,width=16,command=self.exit_fun).grid(row=0,column=4,padx=20,pady=20)

#=============File Frame========================
        File_Frame=Frame(self.root,bd=10,relief=GROOVE)
        File_Frame.place(x=1060,y=102,height=450,width=280)

        ftitle=Label(File_Frame,text="ALL FILES",font=("times new roman",18,"bold"),bd=7,relief=GROOVE).pack(fill=X)

        scroll_y=Scrollbar(File_Frame,orient=VERTICAL)
        self.file_list=Listbox(File_Frame,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()
        self.root.mainloop()


    def save_data(self):
        present="no"
        if self.s_id.get()=="":
           messagebox.showerror("Error","Student Id must be required!!")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:     
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesno("Update","File already present \n Do You want to update it?")
                    if ask>0:
                        self.save_file()
                        messagebox.showinfo("Update","Record has Updated Successfully")
                        self.show_files()
                else:
                    self.save_file()
                    messagebox.showinfo("Saved","Record has saved successfuly")
                    self.show_files()        
            else:
                self.save_file()
                messagebox.showinfo("Saved","Record has saved Successfully")        
        
    def save_file(self):
        f=open("files/"+str(self.s_id.get())+".txt","w")
        f.write(
                str(self.s_id.get())+","+
                str(self.name.get())+","+
                str(self.course.get())+","+
                str(self.address.get())+","+
                str(self.city.get())+","+
                str(self.contact.get())+","+
                str(self.date.get())+","+
                str(self.degree.get())+","+
                str(self.proof.get())+","+
                str(self.payment.get())    
                )
        f.close()
            
    def show_files(self):
        files=os.listdir("files/")
        self.file_list.delete(0,END)
        if len(files)>0:
            for i in files:
                self.file_list.insert(END,i)

    def get_data(self,ev):
        get_cursor=self.file_list.curselection()
        #print(self.file_list.get(get_cursor)) 
        f1=open("files/"+self.file_list.get(get_cursor))
        value=[]
        for f in f1:
            value=f.split(",")

        self.s_id.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.address.set(value[3])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])

    def clear(self):
        self.s_id.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")

    def delete(self):
            present="no"
            if self.s_id.get()=="":
                messagebox.showerror("Error","Student Id must be required!!")
            else:
                f=os.listdir("files/")
                if len(f)>0:
                   for i in f:     
                       if i.split(".")[0] == self.s_id.get():
                           present="yes"
                   if present=="yes":
                        ask=messagebox.askyesno("Delete","Do You really want to delete?")
                        if ask>0:
                            os.remove("files/"+self.s_id.get()+".txt")
                            messagebox.showinfo("Success","Deleted Successfully")
                            self.show_files()
                   else:
                           messagebox.showerror("Error","File not found.")        

    def exit_fun(self):
        ask=messagebox.askyesno("Exit","Do you really want to Exit?")
        if ask>0:
             self.root.destroy()                           

    def logout(self):
        self.root.destroy()
        import login


