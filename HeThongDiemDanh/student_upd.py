import numpy as np
import datetime
from time import strftime
import cv2
import os
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

from MyFuntion import *
from DBConnection import DBConnection
from ADO.StudentDAO import StudentDAO
from ADO.ClassDAO import ClassDAO

mydata = []

BUTTON_FACE = "#EDF1F7"
BLUE = "#08A3D2"


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry(CenterWindowToDisplay(self.root, 1530, 790))
        self.root.title("QLSV")
        self.root.resizable(False, False)
        # student variables
        self.db = DBConnection()
        self.studentDAO = StudentDAO()
        self.classDAO = ClassDAO()
        self.var_dep=StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()

        # classvariables
        self.var_class = StringVar()
        self.var_nameclass = StringVar()

        img3 = PIL.Image.open(r"ImageFaceDetect\bg1.png")
        img3 = img3.resize((1530, 790), PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        # heading
        # ========title=========
        self.heading = Label(self.root, text="Student Management", font=("yu gothic ui", 28, "bold"), 
                             bg=BUTTON_FACE, fg=BLUE, bd=5, relief=FLAT)
        self.heading.place(x=400, y=25, width=650)

        self.main_frame = Frame(bg_img, bd=2, bg=BUTTON_FACE)
        self.main_frame.place(x=23, y=90, width=1482, height=654)

        self.setup_left_frame()

        self.setup_right_frame()

    # left frame
    def setup_left_frame(self):
        self.set_id()
        self.left_frame = LabelFrame(self.main_frame, font=("arial", 12, "bold"), bd=2, bg="white")
        self.left_frame.place(x=10,y=10,width=730,height=646)

        label_Update_att = Label(self.left_frame, text="Student Information", font=("yu gothic ui", 16, "bold"),
                                 bg="white", fg=BLUE)
        label_Update_att.place(x=0, y=1, width=700, height=42)

        self.setup_course_frame()

        self.setup_class_student_frame()
        
    def setup_course_frame(self):
        self.current_course_frame = LabelFrame(self.left_frame, text="Course Information", font=("arial", 12, "bold"),
                                          bd=2, bg="white", relief=RIDGE)
        self.current_course_frame.place(x=5, y=55, width=720, height=130)

        #department
        dep_label=Label(self.current_course_frame, text="Chuyên ngành", font=("arial",13,"bold"), bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(self.current_course_frame, textvariable=self.var_dep, font=("arial",13), 
                               state="readonly", width=20)
        dep_combo["values"] = ("Chọn chuyên ngành","Điện tử viễn thông","IT","Cơ khí","Điện","Kế toán","Tự động hóa")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_label = Label(self.current_course_frame, text="Hệ đào tạo", font=("arial", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(self.current_course_frame, textvariable=self.var_course, font=("arial", 13), 
                                    state="readonly",width=20)
        course_combo["values"] = ("Chọn hệ", "Chính quy", "Liên Thông", "CLC")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #year
        year_label = Label(self.current_course_frame, text="Năm học", font=("arial", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(self.current_course_frame,textvariable=self.var_year, font=("arial", 13), 
                                  state="readonly", width=20)
        year_combo["values"] = ("Chọn năm học", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)


        #semester
        semester_label = Label(self.current_course_frame, text="Học kì", font=("arial", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(self.current_course_frame,textvariable=self.var_semester ,font=("arial", 13), 
                                      state="readonly", width=20)
        semester_combo["values"] = ("Chọn học kì", "Học kì I", "Học kì II")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

    def setup_class_student_frame(self):
        #Class_student
        self.class_student_frame = LabelFrame(self.left_frame, bd=2, bg="white", text="Class Information", font=("arial", 13, "bold"), 
                                         relief=RIDGE)
        self.class_student_frame.place(x=5, y=195, width=720, height=420)

        #student_id
        studentID_label = Label(self.class_student_frame, text="ID Student:", font=("arial", 13, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10,pady=10, sticky=W)

        studentID_entry=ttk.Entry(self.class_student_frame, width=20, textvariable=self.var_std_id,font=("arial", 13, "bold"), 
                                  state="disabled")
        studentID_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #studentName
        studentName_label = Label(self.class_student_frame, text="Name Student:", font=("arial", 13, "bold"),
                                bg="white")
        studentName_label.grid(row=0, column=2, padx=10,pady=10, sticky=W)

        studentName_entry = ttk.Entry(self.class_student_frame, width=20, textvariable=self.var_std_name, font=("arial", 13))
        studentName_entry.grid(row=0, column=3, padx=10,pady=10, sticky=W)

        #class
        class_div_label = Label(self.class_student_frame, text="Class:", font=("arial", 13, "bold"),
                                  bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        class_div_entry = ttk.Entry(self.class_student_frame, width=20, textvariable=self.var_div, font=("arial", 13))
        class_div_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)


        #roll
        roll_no_label = Label(self.class_student_frame, text="ID card:", font=("arial", 13, "bold"),
                                  bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        roll_no_entry = ttk.Entry(self.class_student_frame, width=20,textvariable=self.var_roll ,font=("arial", 13))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        #gender
        gender_label = Label(self.class_student_frame, text="Gender:", font=("arial", 13, "bold"),
                                bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        gender_combo = ttk.Combobox(self.class_student_frame, textvariable=self.var_gender, font=("arial", 13), 
                                    state="readonly", width=18)
        gender_combo["values"] = ("Nam", "Nữ", "Khác")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        #DOB
        dob_label = Label(self.class_student_frame, text="Date of birth:", font=("arial", 13, "bold"),
                              bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        now = datetime.datetime.now()
        self.dob_entry = DateEntry(self.class_student_frame, font=("arial", 13),
                                   width=18, bd=3,selectmode='day',
                                   year=now.year, month=now.month, day=now.day, date_pattern='dd/mm/yyyy')
        self.dob_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        #email
        email_label = Label(self.class_student_frame, text="Email:", font=("arial", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        email_entry = ttk.Entry(self.class_student_frame, width=20, textvariable=self.var_email, font=("arial", 13))
        email_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)


        #Phone
        phone_label = Label(self.class_student_frame, text="Phone number:", font=("arial", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        phone_entry = ttk.Entry(self.class_student_frame, textvariable=self.var_phone, font=("arial", 13), width=20)
        phone_entry.grid(row=3, column=3, padx=10, pady=10, sticky=W)


        #Address
        address_label = Label(self.class_student_frame, text="Địa chỉ:", font=("arial", 13, "bold"),
                            bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        address_entry = ttk.Entry(self.class_student_frame,textvariable=self.var_address ,font=("arial", 13), width=20)
        address_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)


        #radioBtn
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(self.class_student_frame,variable=self.var_radio1,text="Có ảnh",value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2 = ttk.Radiobutton(self.class_student_frame,variable=self.var_radio1, text="Không ảnh", value="No")
        radionbtn2.grid(row=6, column=1)

        self.setup_left_button_frame()

    def setup_left_button_frame(self):
        #btn_frame
        btn_frame = Frame(self.class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=280,width=715,height=35)

        save_btn=Button(btn_frame, text="Save", font=("arial",13,"bold"),
                        bg="#38a6f0", fg="white", width=17,
                        command=self.add_student_data)
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Edit", font=("arial", 13, "bold"), 
                            bg="#38a6f0", fg="white", width=17,
                            command=self.update_student_data)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", font=("arial", 13, "bold"), 
                            bg="#38a6f0", fg="white", width=17,
                            command=self.delete_student_data)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", font=("arial", 13, "bold"), 
                           bg="#38a6f0", fg="white", width=17,
                           command=self.resert_student_data)
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(self.class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=335, width=715, height=35)

        take_photo_btn = Button(btn_frame1, text="Lấy ảnh sinh viên", font=("arial", 13, "bold"), 
                                bg="#38a6f0", fg="white", width=35,command=self.generate_dataset)
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text="Training Data", font=("arial", 13, "bold"), 
                                  bg="#38a6f0", fg="white", width=35,command=self.train_classifier)
        update_photo_btn.grid(row=1, column=1)

    def set_id(self):
        id = self.studentDAO.get_next_id()
        self.var_std_id.set(id)

    def get_cursor_student(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_std_id.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.dob_entry.set_date(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set(data[13]),

    def add_student_data(self):
            list_class = self.classDAO.get_list_class()
            if self.var_dep.get() == "Chọn chuyên ngành" or self.var_std_name.get() == "" or self.var_std_id.get() == "" or self.var_div.get() == "":
                messagebox.showerror("Error","Please enter complete information",parent=self.root)
            elif (self.var_div.get() not in list_class):
                messagebox.showerror("Error", "The class name does not exist ! Please check back", parent=self.root)
            else:
                self.studentDAO.insert(self.var_std_id.get(),
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_std_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.dob_entry.get_date().strftime('%d/%m/%Y'),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_radio1.get())
                self.fetch_student_data()
                self.resert_student_data()
                messagebox.showinfo("Successfully","Add Successfully", parent=self.root)

    def delete_student_data(self):
            if self.var_std_id.get() == "":
                messagebox.showerror("Error","ID must not be empty",parent=self.root)
            else:
                try:
                    delete = messagebox.askyesno("Delete","Do you want to delete?",parent=self.root)
                    if delete > 0:
                        self.studentDAO.delete(self.var_std_id.get())
                    else:
                        if not delete:
                            return
                    self.fetch_student_data()
                    self.resert_student_data()
                    messagebox.showinfo("Delete","Delete successfully",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def search_student_data(self):
                if self.var_com_search.get() == "" or self.var_search.get() == "":
                    messagebox.showerror("Error !", "Please enter complete information",parent=self.root)
                else:
                    try:
                        if (self.var_com_search.get() == "ID Sinh viên"):
                            self.var_com_search.set("Student_id")
                        elif (self.var_com_search.get() == "Tên sinh viên"):
                            self.var_com_search.set("Name")
                        elif (self.var_com_search.get() == "Lớp biên chế"):
                            self.var_com_search.set("Class")
                        data = self.studentDAO.search(str(self.var_com_search.get()), self.var_search.get())
                        if (len(data) != 0):
                            self.student_table.delete(*self.student_table.get_children())
                            for i in data:
                                self.student_table.insert("", END, values=i)
                        else:
                            self.student_table.delete(*self.student_table.get_children())
                            messagebox.showinfo("Notification", "No data",parent=self.root)
                    except Exception as es:
                        messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def update_student_data(self):
        if self.var_dep.get() == "Chọn chuyên ngành" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","Please enter complete information",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update?",parent=self.root)
                if Update > 0:
                    self.studentDAO.update(self.var_dep.get(),
                                           self.var_course.get(),
                                           self.var_year.get(),
                                           self.var_semester.get(),
                                           self.var_std_name.get(),
                                           self.var_div.get(),
                                           self.var_roll.get(),
                                           self.var_gender.get(),
                                           self.dob_entry.get_date().strftime('%d/%m/%Y'),
                                           self.var_email.get(),
                                           self.var_phone.get(),
                                           self.var_address.get(),
                                           self.var_radio1.get(),
                                           self.var_std_id.get())
                else:
                    if not Update:
                        return
                messagebox.showinfo("Successfully","Update Successfully",parent=self.root)
                self.fetch_student_data()
                self.resert_student_data()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def fetch_student_data(self):
        data = self.studentDAO.select()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)

    def resert_student_data(self):
        self.var_dep.set("Chọn chuyên ngành"),
        self.var_course.set("Chọn hệ"),
        self.var_year.set("Chọn năm học"),
        self.var_semester.set("Chọn học kì"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Nam"),
        self.dob_entry.set_date(strftime("%d/%m/%Y")),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),

        self.var_radio1.set(""),
        self.set_id()

    def generate_dataset(self):
        if self.var_dep.get() == "Chọn chuyên ngành" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error","Please enter complete information",parent=self.root)
        else:
            self.studentDAO.update(self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_std_name.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.dob_entry.get_date().strftime('%d/%m/%Y'),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_radio1.get(),
                                self.var_std_id.get())
            self.fetch_student_data()
            self.resert_student_data()
            #=========load haar===================
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                #scaling factor 1.3
                ##minimum neighbor 5
                for(x, y, w, h) in faces:
                    face_cropped=img[y:y+h, x:x+w]
                    return  face_cropped
                
            cap = cv2.VideoCapture(0)
            img_id=0
            while True:
                net, my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id+=1
                    # face=cv2.resize(face_cropped(my_frame),(190,190))
                    face = cv2.cvtColor(face_cropped(my_frame),cv2.COLOR_BGR2GRAY)
                    fill_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"

                    cv2.imwrite(fill_name_path,face)
                    cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
                    cv2.imshow("Cropped Face",face)

                if cv2.waitKey(1) == 13 or int(img_id) == 120:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Kết quả","Tạo dữ liệu khuôn mặt Successfully",parent=self.root)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=PIL.Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #=================Train data classifier and save============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Kết quả","Training dataset Completed", parent=self.root)

    # right_frame
    def setup_right_frame(self):
        self.right_frame = LabelFrame(self.main_frame, bd=2, bg="white", font=("arial", 12, "bold"))
        self.right_frame.place(x=750, y=10, width=720, height=330)

        self.setup_search_frame()

        self.setup_table_frame()

        self.setup_class_frame()

    def setup_search_frame(self):
        self.search_frame = LabelFrame(self.right_frame, text="Search System", font=("yu gothic ui", 13, "bold"), 
                                  bd=2, bg="white", relief=RIDGE)
        self.search_frame.place(x=5, y=5, width=710, height=70)

        self.var_com_search= StringVar()
        search_label = Label(self.search_frame, text="Search by :", font=("arial", 13, "bold"),
                             bg="white",fg=BLUE)
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(self.search_frame, font=("arial", 13), state="readonly",
                                      width=13, textvariable=self.var_com_search)
        search_combo["values"] = ("ID Sinh viên", "Tên sinh viên", "Lớp biên chế")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(self.search_frame, width=15, font=("arial", 13),textvariable=self.var_search)
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(self.search_frame, text="Search", font=("arial", 12, "bold"),
                            bg="#38a6f0", fg="white", width=12,
                            command=self.search_student_data)
        search_btn.grid(row=0, column=3,padx=4)

        showAll_btn = Button(self.search_frame, text="All", font=("arial", 12, "bold"), 
                             bg="#38a6f0", fg="white", width=12,
                             command=self.fetch_student_data)
        showAll_btn.grid(row=0, column=4,padx=4)

    def setup_table_frame(self):
        self.table_frame = Frame(self.right_frame, bd=2, bg="white", relief=RIDGE)
        self.table_frame.place(x=5, y=85, width=710, height=230)

        scroll_x=ttk.Scrollbar(self.table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(self.table_frame,column=(
            "id","dep","course","year","sem","name","div","roll","gender","dob","email","phone","address","photo"
            ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="ID Sinh viên")
        self.student_table.heading("dep",text="Chuyên ngành")
        self.student_table.heading("course", text="Chương trình học")
        self.student_table.heading("year", text="Năm học")
        self.student_table.heading("sem", text="Học kì")
        self.student_table.heading("name", text="Họ tên")
        self.student_table.heading("div", text="Lớp biên chế")
        self.student_table.heading("roll", text="CMND")
        self.student_table.heading("gender", text="Giới tính")
        self.student_table.heading("dob", text="Ngày sinh")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Số điện thoại")
        self.student_table.heading("address",text="Địa chỉ")

        self.student_table.heading("photo", text="Trạng thái ảnh")
        self.student_table["show"]="headings"

        self.student_table.column("id", width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor_student)
        self.fetch_student_data()
        self.set_id()

    def setup_class_frame(self):
        self.class_frame = LabelFrame(self.main_frame, bd=2, bg="white", relief=RIDGE,
                                      font=("yu gothic ui", 12, "bold"))
        self.class_frame.place(x=750, y=345, width=720, height=310)

        label_studentsb = Label(self.class_frame, bg="white", fg=BLUE, text="Class Management",
                                font=("yu gothic ui", 14, "bold"))
        label_studentsb.place(x=0, y=1, width=700, height=35)

        # search
        search_frame = Frame(self.class_frame, bg="white", relief=RIDGE)
        search_frame.place(x=5, y=35)
        search_label = Label(search_frame, text="Search by :", font=("arial", 12, "bold"),
                             bg="white",fg=BLUE)
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.var_com_searchclass = StringVar()
        search_combo = ttk.Combobox(search_frame, font=("arial", 12),
                                    state="readonly", width=15,
                                    textvariable=self.var_com_searchclass)
        search_combo["values"] = ("Lớp", "Tên lớp")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.var_searchclass = StringVar()
        searchstd_entry = ttk.Entry(search_frame, textvariable=self.var_searchclass, width=20,
                                    font=("arial", 11))
        searchstd_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        searchstd_btn = Button(search_frame, text="Search",
                               font=("arial", 11, "bold"), 
                               bg="#38a6f0", fg="white", width=12, 
                               command=self.search_class_data)
        searchstd_btn.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        showAllstd_btn = Button(search_frame, text="All", font=("arial", 11, "bold"), 
                                bg="#38a6f0", fg="white", width=12, 
                                command=self.fetch_class_data)
        showAllstd_btn.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        # subject
        info_frame = Frame(self.class_frame, bg="white", relief=RIDGE)
        info_frame.place(x=5, y=80)
        subject_id_label = Label(info_frame, text="Class:", font=("arial", 12, "bold"), bg="white", width=12)
        # studentid_label.place(x=20, y=120, width=100)
        subject_id_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        subject_id_entry = ttk.Entry(info_frame, textvariable=self.var_class, font=("arial", 12), width=20)
        subject_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # subject
        sub_name_label = Label(info_frame, text="Class name:", font=("arial", 12, "bold"), bg="white")
        sub_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        sub_name_entry = ttk.Entry(info_frame, font=("arial", 12), width=20, textvariable=self.var_nameclass)
        sub_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        
        # btn_frameteacher
        btn_framestd = Frame(self.class_frame, bg="white", relief=RIDGE)
        btn_framestd.place(x=30, y=150)

        addTc_btn = Button(btn_framestd, text="Add",
                           font=("arial", 12, "bold"),
                           bg="#fbd568", fg="#996319", width=12, 
                           command=self.add_class_data)
        addTc_btn.grid(row=0, column=0, pady=10, padx=5)

        deleteTc_btn = Button(btn_framestd, text="Delete", font=("arial", 12, "bold"),
                              bg="#fbd568", fg="#996319", width=12, 
                              command=self.delete_class_data)
        deleteTc_btn.grid(row=0, column=1, pady=10, padx=5)

        updateTc_btn = Button(btn_framestd, text="Edit", font=("arial", 12, "bold"),
                              bg="#fbd568", fg="#996319", width=12, 
                              command=self.update_class_data)
        updateTc_btn.grid(row=1, column=0, pady=10, padx=5)

        resetTc_btn = Button(btn_framestd, text="Reset", font=("arial", 12, "bold"),
                             bg="#fbd568", fg="#996319", width=12, 
                             command=self.reset_class_data)
        resetTc_btn.grid(row=1, column=1, pady=10, padx=5)

        # table_frame
        tablestd_frame = Frame(self.class_frame, bd=2, relief=RIDGE, bg="white")
        tablestd_frame.place(x=350, y=80, width=350, height=200)

        # scroll bar
        scroll_x = ttk.Scrollbar(tablestd_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tablestd_frame, orient=VERTICAL)

        self.StudentTable = ttk.Treeview(tablestd_frame, column=("class", "name"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)

        self.StudentTable.heading("class", text="Lớp học")
        self.StudentTable.heading("name", text="Tên")

        self.StudentTable["show"] = "headings"
        self.StudentTable.column("class", width=80)
        self.StudentTable.column("name", width=80)

        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease>", self.get_cursor_class)
        self.fetch_class_data()

    def get_cursor_class(self, event=""):
            cursor_row = self.StudentTable.focus()
            content = self.StudentTable.item(cursor_row)
            rows = content['values']
            self.var_class.set(rows[0])
            self.var_nameclass.set(rows[1])

    def add_class_data(self):
        list_class = self.classDAO.get_list_class()
        if self.var_class.get() == "" or self.var_nameclass.get() == "":
            messagebox.showerror("Error", "Please enter complete information", parent=self.root)

        elif (self.var_class.get()  in list_class):
            messagebox.showerror("Error", "Class already exists! Please check back", parent=self.root)
        else:
            try:
                self.classDAO.insert(self.var_class.get(), self.var_nameclass.get())
                self.fetch_class_data()
                self.reset_class_data()
                messagebox.showinfo("Successfully", "Add uccessfully",
                                    parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def delete_class_data(self):
        if self.var_class == "" or self.var_nameclass.get() == "":
            messagebox.showerror("Error", "Information must be not empty! ", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete??", parent=self.root)
                if delete > 0:
                    self.classDAO.delete(self.var_class.get())
                else:
                    if not delete:
                        return
                messagebox.showinfo("Delete", "Delete successfully", parent=self.root)
                self.reset_class_data()
                self.fetch_class_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def update_class_data(self):
        if self.var_class == "" or self.var_nameclass.get() == "":
            messagebox.showerror("Error", "Please enter complete information", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Bạn có muốn cập nhật bản ghi này không?", parent=self.root)
                if Update > 0:
                    self.classDAO.update(self.var_nameclass.get(), self.var_class.get())
                else:
                    if not Update:
                        return
                messagebox.showinfo("Successfully", "Update successfully",
                                    parent=self.root)
                self.reset_class_data()
                self.fetch_class_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def search_class_data(self):
            if self.var_com_searchclass.get() == "" or self.var_searchclass.get() == "":
                messagebox.showerror("Error !", "Please enter complete information",parent=self.root)
            else:
                try:
                    if (self.var_com_searchclass.get() == "Lớp"):
                        self.var_com_searchclass.set("Class")
                    elif (self.var_com_searchclass.get() == "Tên lớp"):
                        self.var_com_searchclass.set("Name")
                    data = self.classDAO.search(str(self.var_com_searchclass.get()), str(self.var_searchclass.get()))
                    if (len(data) != 0):
                        self.StudentTable.delete(*self.StudentTable.get_children())
                        for i in data:
                            self.StudentTable.insert("", END, values=i)
                    else:
                        self.StudentTable.delete(*self.StudentTable.get_children())
                        messagebox.showinfo("Notification", "No data",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def fetch_class_data(self):
            data = self.classDAO.select()
            if len(data) != 0:
                self.StudentTable.delete(*self.StudentTable.get_children())
                for i in data:
                    self.StudentTable.insert("", END, values=i)
                    mydata.append(i)

    def reset_class_data(self):
        self.var_class.set("")
        self.var_nameclass.set("")

if __name__=="__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()
