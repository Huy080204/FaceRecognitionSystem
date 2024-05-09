from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from ADO.TeacherDAO import TeacherDAO
from DBConnection import DBConnection

from main import Face_Recognition_System
from main import new_print
from MyFuntion import *

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry(CenterWindowToDisplay(self.root, 450, 500))

        # =============variable============
        self.db = DBConnection()
        self.teacher_DAO = TeacherDAO()
        self.var_email = StringVar()
        self.var_password = StringVar()

        #===========Frame============
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=0,y=0,width=450,height=500)

        #===========style_ttk.entry===========
        self.estyle = ttk.Style()
        self.estyle.configure("EntryStyle.TEntry", background='black')

        title = Label(login_frame, text="Login", font=("arial",30,"bold"),bg="white",fg="#08A3D2")
        title.place(x=50,y=40)

        email = Label(login_frame, text="Email", font=("arial", 13, "bold"), bg="white", fg="gray")
        email.place(x=50, y=130)

        self.txtuser=ttk.Entry(login_frame,textvariable=self.var_email, font=("arial", 15))
        self.txtuser.place(x=50, y=160,height=35,width=350)

        pass_word = Label(login_frame, text="Password", font=("arial", 13, "bold"), bg="white", fg="gray")
        pass_word.place(x=50, y=220)

        self.txtpass = ttk.Entry(login_frame, textvariable=self.var_password,font=("arial", 15), background="black" ,show="*")
        self.txtpass.place(x=50, y=250,height=35,width=350)

        # =============check_button=============
        self.varcheck = IntVar()
        checkbtn = Checkbutton(login_frame, variable=self.varcheck, text="Login with Admin account",
                               font=("arial", 12), onvalue=1, offvalue=0, bg="white")
        checkbtn.place(x=50, y=320)

        # =============login_button=============
        btn_login = Button(login_frame, text="Login",font=("arial", 17,"bold"), 
                           fg="white", bd=0, bg="#08A3D2", cursor="hand2", 
                           command=self.login)
        btn_login.place(x=120, y=400,width=220,height=40)

        
    def reset(self):
        self.var_email.set("")
        self.var_password.set("")
        self.varcheck.set(0)


    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get()== "":
            messagebox.showerror("Error !!","Please fill all information")
        elif(self.varcheck.get() == 1):
            self.db.connect()
            self.db.my_cursor.execute("select * from admin where Account=%s and Password=%s", (
                self.var_email.get(),
                self.var_password.get()
            ))
            row = self.db.my_cursor.fetchone()
            self.set_new_window(row)
            self.db.close()
        else:
            row = self.teacher_DAO.get_id_by_email_and_password(self.var_email.get(), self.var_password.get())
            self.set_new_window(row)


    def set_new_window(self, row):
        if row == None:
            messagebox.showerror("Error", "Wrong email or password")
        else:
            new_print(str(row[0]))
            self.reset()
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition_System(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()