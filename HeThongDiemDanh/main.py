import os
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import messagebox

from student_upd import Student
from face_recognition import Face_Recognition
from face_recognition import new_tcid
from attendance import Attendance
from subject import Subject
from teacher import Teacher
from lesson import Lesson
from report_attendance import Report

from DBConnection import DBConnection
from MyFuntion import *

value_from_p1 = None
BUTTON_FACE = "#EDF1F7"
BLUE = "#08A3D2"

def new_print(value):
    global value_from_p1
    if value == "admin":
        value = "0"
    value_from_p1 = value
    print(value_from_p1)


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry(CenterWindowToDisplay(self.root, 1530, 790))
        self.root.title("Face recognition system")
        self.root.resizable(False, False)
        self.db = DBConnection()
        self.images = {}

        new_tcid(value_from_p1)
        #background
        print(value_from_p1)

        img3 = PIL.Image.open(r"ImageFaceDetect\bgbtn.png")
        img3 = img3.resize((1530, 790), PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        self.setup_header()

        self.setup_main()


    def setup_header(self):
        #====title=========
        self.heading = Label(self.root, 
                             text="Face recognition system", font=("yu gothic ui", 30, "bold"), 
                             bg=BUTTON_FACE, fg=BLUE,
                             bd=5, relief=FLAT)
        self.heading.place(x=150, y=50, width=500)

        #=========account===========
        self.account = self.get_role()
        img_user = PIL.Image.open(r"ImageFaceDetect\user.png")
        img_user = img_user.resize((27, 27), PIL.Image.LANCZOS)
        self.img_user = ImageTk.PhotoImage(img_user)
        self.lblemail = Label(self.root, text=self.account, font=("yu gothic ui", 14, "bold"), 
                              bg=BUTTON_FACE, fg="black", 
                              image=self.img_user, compound="left", padx=10)
        self.lblemail.place(x=150, y=125, width=200, height=28)

        #=======logout==========
        img_logout = PIL.Image.open(r"ImageFaceDetect\logout.png")
        img_logout = img_logout.resize((27, 27), PIL.Image.LANCZOS)
        self.photoimglogout = ImageTk.PhotoImage(img_logout)

        b1_1 = Button(self.root, text="Logout", font=("arial", 13, "bold"), cursor="hand2",
                      image=self.photoimglogout, compound="left", padx=10,
                      bg=BUTTON_FACE, fg="black", activebackground=BUTTON_FACE, borderwidth=0, command=self.exit)
        b1_1.place(x=1350, y=48, width=100, height=27)

    def get_role(self):
        if(value_from_p1 == "0"):
            return "Admin"
        elif(value_from_p1 == None):
            return "AdminSafe"
        else:
            self.db.connect()
            self.db.my_cursor.execute("select Email from teacher where Teacher_id=%s", (
                value_from_p1,
            ))
            row = self.db.my_cursor.fetchone()
            self.db.conn.close()
            return row[0]

    def setup_main(self):
        #============student================
        self.btn_student = self.setup_button("student.png", "Student", self.student_details)
        self.btn_student.place(x=179, y=200, width=175, height=175)

        #============nhan dien============
        self.btn_recognition = self.setup_button("face-recognition.png", "Recognition", self.face_recognition)
        self.btn_recognition.place(x=520, y=200, width=175, height=175)

        #===========diem-danh===============
        self.btn_attendance = self.setup_button("attendance.png", "Attendance", self.attendance_data)
        self.btn_attendance.place(x=857, y=200, width=175, height=175)

        #==========mon hoc=================
        self.btn_subject = self.setup_button("book.png", "Subject", self.subject_data)
        self.btn_subject.place(x=1175, y=200, width=175, height=175)

        #==========giaovien=============
        self.btn_teacher = self.setup_button("teacher.png", "Teacher", self.teacher_data)
        self.btn_teacher.place(x=520, y=493, width=175, height=175)

        #==========thongke=============
        self.btn_statictical = self.setup_button("statictical.png", "Statictical", self.report_data)
        self.btn_statictical.place(x=183, y=490, width=175, height=175)

        #==========buoi hoc================
        self.btn_lession = self.setup_button("lesson.png", "Lesson", self.lesson_data)
        self.btn_lession.place(x=855, y=493, width=175, height=175)

        #==========Xem Anh===============
        self.btn_picture = self.setup_button("picture.png", "Picture", self.open_img)
        self.btn_picture.place(x=1175, y=493, width=175, height=175)

        if(value_from_p1 == "0" or value_from_p1 == None):
            self.btn_teacher['state'] = "normal"
            self.btn_picture['state'] = "normal"
        else:
            self.btn_teacher['state'] = "disabled"
            self.btn_picture['state'] = "disabled"

    def setup_button(self, img_str, text, func):
        img_str = fr"ImageFaceDetect\{img_str}"

        if img_str not in self.images:
            img_btn = PIL.Image.open(img_str)
            img_btn = img_btn.resize((100, 100), PIL.Image.LANCZOS)
            self.images[img_str] = ImageTk.PhotoImage(img_btn)

        btn = Button(self.root, text=text, font=("yu gothic ui", 16, "bold"),
                      image=self.images[img_str], pady=5,
                      activebackground="white", bg="white",
                      compound="top", borderwidth=0, cursor="hand2",
                      command=func)
        return btn

    # command
    def exit(self):
        Exit = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=self.root)
        if(Exit > 0):
            self.root.destroy()
        else:
            if not Exit:
                return
            
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def report_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Report(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def subject_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Subject(self.new_window)

    def teacher_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Teacher(self.new_window)

    def lesson_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Lesson(self.new_window)

    def open_img(self):
        os.startfile("data")


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()