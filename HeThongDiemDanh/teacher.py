from PIL import ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PIL.Image

from MyFuntion import *
from ADO.TeacherDAO import TeacherDAO


mydata=[]
BUTTON_FACE = "#EDF1F7"
BLUE = "#08A3D2"


class Teacher:
    def __init__(self,root):
        self.root=root
        self.root.geometry(CenterWindowToDisplay(self.root, 1530, 790))
        self.root.title("Face recognition system")
        self.root.resizable(False, False)

        # variable
        self.teacherDAO = TeacherDAO()
        self.var_name = StringVar()
        self.var_id = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # bg
        img3 = PIL.Image.open(r"ImageFaceDetect\bg1.png")
        img3 = img3.resize((1530, 790), PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        # heading
        self.heading = Label(self.root, text="Teacher Information Management", font=("yu gothic ui", 28, "bold"), bg=BUTTON_FACE, fg=BLUE,
                             bd=5, relief=FLAT)
        self.heading.place(x=400, y=25, width=650)

        # main frame
        self.main_frame = Frame(bg_img, bd=2, bg=BUTTON_FACE)
        self.main_frame.place(x=23, y=102, width=1482, height=671)

        self.setup_left_frame()

        self.setup_right_frame()

    def setup_left_frame(self):
        self.set_id()

        self.left_frame = LabelFrame(self.main_frame, bd=2, bg="white", relief=RIDGE,
                                font=("arial", 12, "bold"))
        self.left_frame.place(x=20, y=5, width=450, height=650)

        label_Update_att = Label(self.left_frame, bg="#CCE5FF", fg="black", text="Teacher Information",
                                 font=("arial", 18, "bold"))
        label_Update_att.place(x=0, y=1, width=446, height=45)

        left_inside_frame = Frame(self.left_frame, bd=1, bg="white")
        left_inside_frame.place(x=0, y=60, width=430, height=570)

        # idgv
        id_label = Label(left_inside_frame, text="ID teacher:",font=("arial", 12, "bold"),
                                    bg="white")
        id_label.grid(row=0, column=0, padx=20, pady=10, sticky=W)

        id_entry = ttk.Entry(left_inside_frame, textvariable=self.var_id,state="disabled",
                                        font=("arial", 12, "bold"), width=22)
        id_entry.grid(row=0, column=1, padx=20, pady=10, sticky=W)

        # idstudent
        name_label = Label(left_inside_frame, text="Name:", font=("arial", 12, "bold"),
                           bg="white")
        name_label.grid(row=1, column=0, padx=20, pady=10, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_name,
                               font=("arial", 12))
        name_entry.grid(row=1, column=1, padx=20, pady=10, sticky=W)

        # name
        phone_label = Label(left_inside_frame, text="Phone:", font=("arial", 12, "bold"),
                          bg="white")
        phone_label.grid(row=2, column=0, padx=20, pady=10, sticky=W)

        phone_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_phone,
                                    font=("arial", 12))
        phone_entry.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        # email
        email_label = Label(left_inside_frame, text="Email:", font=("arial", 12, "bold"),
                           bg="white")
        email_label.grid(row=3, column=0, padx=20, pady=10, sticky=W)

        email_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_email,
                                     font=("arial", 12))
        email_entry.grid(row=3, column=1, padx=20, pady=10, sticky=W)

        # password
        passLabel = Label(left_inside_frame, text="Password:", font=("arial", 12, "bold"),
                                 bg="white")
        passLabel.grid(row=6, column=0, padx=20, pady=5, sticky=W)

        passLabel_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_pass,
                                    font=("arial", 12))
        passLabel_entry.grid(row=6, column=1, padx=20, pady=5, sticky=W)

        # =====btn_frame============
        btn_frame = Frame(left_inside_frame, bg="white")
        btn_frame.place(x=0, y=350, width=440, height=115)

        add_btn = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 13, "bold"),
                            bg=BLUE, fg="white", width=17)
        add_btn.grid(row=9, column=0, pady=10,padx=20)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data,
                            font=("arial", 13, "bold"),
                            bg=BLUE, fg="white", width=17)
        delete_btn.grid(row=9, column=1, pady=10,padx=20)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("arial", 13, "bold"),
                            bg=BLUE, fg="white", width=17)
        update_btn.grid(row=10, column=0, pady=20, padx=20)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 13, "bold"),
                           bg=BLUE, fg="white", width=17)
        reset_btn.grid(row=10, column=1, pady=0,padx=20)

    def setup_right_frame(self):
        self.right_frame = LabelFrame(self.main_frame, bd=2, bg="white",
                                 font=("arial", 12, "bold"))
        self.right_frame.place(x=500, y=5, width=960, height=650)

        # search
        self.var_com_search = StringVar()
        search_label = Label(self.right_frame, text="Search by :", font=("arial", 13, "bold"),
                             bg="white")
        search_label.grid(row=0, column=0, padx=15, pady=5, sticky=W)

        search_combo = ttk.Combobox(self.right_frame, font=("arial", 13), textvariable=self.var_com_search,
                                    state="read only",
                                    width=13)
        search_combo["values"] = ("ID teacher", "Name", "Phone number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=15, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(self.right_frame, textvariable=self.var_search, width=15,
                                 font=("arial", 13))
        search_entry.grid(row=0, column=2, padx=15, pady=5, sticky=W)

        search_btn = Button(self.right_frame, command=self.search_data, text="Search",
                            font=("arial", 13, "bold"), bg=BLUE, fg="white",
                            width=12)
        search_btn.grid(row=0, column=3, padx=15)



        showAll_btn = Button(self.right_frame, text="All", command=self.fetch_data,
                             font=("arial", 13, "bold"), bg=BLUE,
                             fg="white",
                             width=12)
        showAll_btn.grid(row=0, column=5, padx=15)

        # table_frame
        table_frame = Frame(self.right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=55, width=940, height=580)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "name", "phone", "email", "pass"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="ID teacher")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("phone", text="Phone number")
        self.AttendanceReportTable.heading("email", text="Email")
        self.AttendanceReportTable.heading("pass", text="Password")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("phone", width=100)
        self.AttendanceReportTable.column("email", width=100)
        self.AttendanceReportTable.column("pass", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def set_id(self):
        id = self.teacherDAO.get_next_id()
        self.var_id.set(id)

    def get_cursor(self, event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_phone.set(rows[2])
        self.var_email.set(rows[3])
        self.var_pass.set(rows[4])

    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_pass.set("")
        self.set_id()

    def fetch_data(self):
        data = self.teacherDAO.select()
        if len(data) != 0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("", END, values=i)
                mydata.append(i)

    def add_data(self):
        if self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error","Please enter complete information",parent=self.root)
        else:
            try:
                self.teacherDAO.insert(
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_pass.get(),                 
                )
                self.fetch_data()
                self.reset_data()
                messagebox.showinfo("Successfully","Add successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)

    def delete_data(self):
            if self.var_id == "":
                messagebox.showerror("Error", "ID must not be empty", parent=self.root)
            else:
                try:
                    delete = messagebox.askyesno("Delete", "Do you want to delete?", parent=self.root)
                    if delete > 0:
                        self.teacherDAO.delete(self.var_id.get())
                    else:
                        if not delete:
                            return
                    messagebox.showinfo("Delete", "Delete successfully", parent=self.root)
                    self.fetch_data()
                    self.reset_data()
                except Exception as es:
                    messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def update_data(self):
        if  self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error","Please enter complete information",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update?", parent=self.root)
                if Update > 0:
                    self.teacherDAO.update(
                        self.var_name.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_pass.get(),
                        self.var_id.get(),
                    )
                else:
                    if not Update:
                        return
                messagebox.showinfo("Successfully","Update successfully",parent=self.root)
                self.fetch_data()
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error !","Please enter complete information")
        else:
            try:
                if(self.var_com_search.get() == "ID GV"):
                    self.var_com_search.set("Teacher_id")
                elif(self.var_com_search.get() == "Tên GV"):
                    self.var_com_search.set("Name")
                elif(self.var_com_search.get()=="SĐT"):
                    self.var_com_search.set("Phone")
                data = self.teacherDAO.search(str(self.var_com_search.get()), self.var_search.get())
                if(len(data)!=0):
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    for i in data:
                        self.AttendanceReportTable.insert("",END,values=i)
                else:
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    messagebox.showinfo("Notification", "No data",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

if __name__=="__main__":
    root=Tk() 
    obj=Teacher(root)
    root.mainloop()