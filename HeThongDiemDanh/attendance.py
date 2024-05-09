import os
from tkinter import *
from tkinter import ttk
import PIL.Image
import PIL.ImageTk
import random
from tkinter import messagebox
import mysql.connector
import numpy as np
from PIL import Image, ImageTk
import cv2

from datetime import datetime
from time import strftime
import csv
from tkinter import filedialog
from MyFuntion import *
from DBConnection import DBConnection
import sys

BUTTON_FACE = "#EDF1F7"
BLUE = "#08A3D2"
RED = "#A91D3A"

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry(CenterWindowToDisplay(self.root, 1530, 790))
        self.root.title("FACE RECOGNIZER")
        self.root.resizable(False, False)
        self.isClicked=False
        today = strftime("%d-%m-%Y")


        #===========variables=========
        self.db = DBConnection()
        self.var_atten_id=StringVar()
        self.var_atten_class = StringVar()
        self.var_atten_idsv = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_timein = StringVar()
        self.var_atten_timeout = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        self.var_atten_lesson=StringVar()

        img3 = PIL.Image.open(r"ImageFaceDetect\bg1.png")
        img3 = img3.resize((1530, 790), PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        # ==================================heading====================================
        # ====title=========
        self.txt = "Manage attendance information"
        self.heading = Label(self.root, text="Manage attendance information", font=("yu gothic ui", 28, "bold"), 
                             bg=BUTTON_FACE, fg=BLUE, bd=5, relief=FLAT)
        self.heading.place(x=400, y=25, width=650)

        main_frame = Frame(bg_img, bd=2, bg=BUTTON_FACE)
        main_frame.place(x=23, y=102, width=1482, height=671)

        # left_label
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=20, y=5, width=450, height=650)

        label_Update_att=Label(Left_frame,text="Cập Nhật điểm danh",font=("times new roman", 18, "bold"),
                               bg="#F0FFF0",fg="#483D8B")
        label_Update_att.place(x=0,y=1,width=446,height=45)

        left_inside_frame = Frame(Left_frame, bd=1, bg="white")
        left_inside_frame.place(x=0, y=60, width=430, height=570)

        #auttenID
        auttendanceID_label = Label(left_inside_frame, text="ID Điểm Danh:", font=("times new roman", 12, "bold"),
                                bg="white")
        auttendanceID_label.grid(row=0, column=0, padx=20, pady=5, sticky=W)

        auttendanceID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, 
                                        font=("times new roman", 12, "bold"), 
                                        state="readonly")
        auttendanceID_entry.grid(row=0, column=1, padx=20, pady=5, sticky=W)


        #idstudent
        roll_label = Label(left_inside_frame, text="ID Sinh viên:", 
                           font=("times new roman", 12, "bold"),
                           bg="white")
        roll_label.grid(row=1, column=0, padx=20, pady=5, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_idsv,
                               font=("times new roman", 12, "bold"), 
                               state="readonly", width=20)
        roll_entry.grid(row=1, column=1, padx=20, pady=5, sticky=W)



        #name
        nameLabel = Label(left_inside_frame, text="Tên sinh viên:", 
                          font=("times new roman", 12, "bold"),
                          bg="white")
        nameLabel.grid(row=2, column=0, padx=20, pady=5, sticky=W)

        nameLabel_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_name,
                                        font=("times new roman", 12, "bold"), 
                                        state="readonly", width=20)
        nameLabel_entry.grid(row=2, column=1, padx=20, pady=5, sticky=W)



        #class
        classLabel = Label(left_inside_frame, text="Lớp học:", 
                           font=("times new roman", 12, "bold"),
                           bg="white")
        classLabel.grid(row=3, column=0, padx=20, pady=5, sticky=W)

        classLabel_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_class,
                                     font=("times new roman", 12, "bold"),
                                     state="readonly")
        classLabel_entry.grid(row=3, column=1, padx=20, pady=5, sticky=W)

        #time_in
        timeLabel = Label(left_inside_frame, text="Giờ vào:", font=("times new roman", 12, "bold"), bg="white")
        timeLabel.grid(row=4, column=0, padx=20, pady=5, sticky=W)

        timeLabel_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_timein,
                                    font=("times new roman", 12, "bold"), width=20)
        timeLabel_entry.grid(row=4, column=1, padx=20, pady=5, sticky=W)

        # time_out
        timeoutLabel = Label(left_inside_frame, text="Giờ ra:", font=("times new roman", 12, "bold"), bg="white")
        timeoutLabel.grid(row=5, column=0, padx=20, pady=5, sticky=W)

        timeoutLabel_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_timeout,
                                    font=("times new roman", 12, "bold"))
        timeoutLabel_entry.grid(row=5, column=1, padx=20, pady=5, sticky=W)

        #date
        dateLabel = Label(left_inside_frame, text="Ngày:", font=("times new roman", 12, "bold"),
                          bg="white")
        dateLabel.grid(row=6, column=0, padx=20, pady=5, sticky=W)

        dateLabel_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date,
                                    font=("times new roman", 12, "bold"),state="readonly")
        dateLabel_entry.grid(row=6, column=1, padx=20, pady=5, sticky=W)

        #auttendance
        auttendanceLabel = Label(left_inside_frame, text="Điểm danh:", font=("times new roman", 12, "bold"),
                           bg="white")
        auttendanceLabel.grid(row=7, column=0,  padx=20, pady=5, sticky=W)

        self.atten_status=ttk.Entry(left_inside_frame, textvariable=self.var_atten_attendance, 
                                    font=("times new roman", 12, "bold"), width=20)

        self.atten_status.grid(row=7,column=1,pady=5,padx=20)



        #lesson
        lessonLabel = Label(left_inside_frame, text="ID Bài học:", font=("times new roman", 12, "bold"), bg="white")
        lessonLabel.grid(row=8, column=0, padx=20, pady=5, sticky=W)

        self.lesson = ttk.Entry(left_inside_frame, textvariable=self.var_atten_lesson, font=("times new roman", 12, "bold"),
                                state="readonly", width=20)
        self.lesson.grid(row=8, column=1, pady=5, padx=20)



        # btn_frame
        label_Update_att = Button(Left_frame, text="Xem ảnh", font=("times new roman", 14, "bold"), 
                                  bg=BLUE, fg="white",
                                  command=self.openImage)
        label_Update_att.place(x=100, y=500, width=250, height=45)
        update_btn = Button(Left_frame, text="Xóa", font=("times new roman", 14, "bold"),
                            bg=RED, fg="white", width=250, 
                            command=self.delete_data)
        update_btn.place(x=100, y=580,width=250,height=45 )


        btn_frame = Frame(left_inside_frame, bg="white")
        btn_frame.place(x=0, y=330, width=440, height=105)

        save_btn = Button(btn_frame, text="Nhập file CSV", font=("times new roman", 13, "bold"), 
                          bg="#38a6f0", fg="white", width=17,
                          command=self.importCsv)
        save_btn.grid(row=9, column=0,padx=20)

        update_btn = Button(btn_frame, text="Xuất file CSV", font=("times new roman", 13, "bold"),
                            bg="#38a6f0", fg="white", width=17,
                            command=self.exportCsv)
        update_btn.grid(row=9, column=1,padx=20)

        delete_btn = Button(btn_frame, text="Cập nhật", font=("times new roman", 13, "bold"),
                            bg="#fbd568", fg="#996319", width=17,
                            command=self.update_data)
        delete_btn.grid(row=10, column=0,pady=10)

        reset_btn = Button(btn_frame, text="Làm mới", font=("times new roman", 13, "bold"),
                           bg="#fbd568", fg="#996319", width=17,
                           command=self.reset_data)
        reset_btn.grid(row=10, column=1,pady=10)

        #right_ label
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", font=("times new roman", 12, "bold"))
        Right_frame.place(x=500, y=5, width=960, height=650)

        #search
        self.var_com_search=StringVar()
        search_label = Label(Right_frame, text="Tìm kiếm theo :", font=("times new roman", 13, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=15, pady=5, sticky=W)

        search_combo = ttk.Combobox(Right_frame, font=("times new roman", 13, "bold"), textvariable=self.var_com_search, 
                                    state="read only", width=13)
        search_combo["values"] = ("ID Điểm Danh", "Ngày", "ID Sinh Viên","ID Buổi học")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=15, sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(Right_frame,textvariable=self.var_search, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=15, pady=5, sticky=W)

        search_btn = Button(Right_frame,command=self.search_data, text="Tìm kiếm", font=("times new roman", 13, "bold"), 
                            bg="#38a6f0", fg="white", width=12)
        search_btn.grid(row=0, column=3, padx=15)

        Today_btn = Button(Right_frame, text="Hôm nay", font=("times new roman", 13, "bold"), 
                           bg="#38a6f0", fg="white", width=12,
                           command=self.today_data)
        Today_btn.grid(row=0, column=4, padx=15)


        showAll_btn = Button(Right_frame, text="Xem tất cả",font=("times new roman", 13, "bold"), 
                             bg="#38a6f0", fg="white", width=12, 
                             command=self.fetch_data)
        showAll_btn.grid(row=0, column=5, padx=15)


        #table_frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=55, width=940, height=580)

        #scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=(
            "id","idsv","name","class","time_in","time_out","date","lesson","attendance"
            ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="AttendanceID")
        self.AttendanceReportTable.heading("idsv", text="ID Sinh Viên")
        self.AttendanceReportTable.heading("name", text="Tên Sinh Viên")
        self.AttendanceReportTable.heading("class", text="Lớp học")
        self.AttendanceReportTable.heading("time_in", text="Giờ vào")
        self.AttendanceReportTable.heading("time_out", text="Giờ ra")
        self.AttendanceReportTable.heading("date", text="Ngày")
        self.AttendanceReportTable.heading("attendance", text="Điểm danh")
        self.AttendanceReportTable.heading("lesson", text="ID Bài học")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("idsv", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("class", width=100)
        self.AttendanceReportTable.column("time_in", width=100)
        self.AttendanceReportTable.column("time_out", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        self.AttendanceReportTable.column("lesson", width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()  # load du lieu len grid
        #================fetchData======================

        # =======================fetch-data========================
    def fetch_data(self):
            # global mydata
            mydata.clear()
            self.db.connect()
            self.db.my_cursor.execute("Select * from attendance")
            data = self.db.my_cursor.fetchall()

            if len(data) != 0:
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in data:

                    self.AttendanceReportTable.insert("", END, values=i)
                    mydata.append(i)


                self.db.conn.commit()
            self.db.conn.close()
    #update du lieu chuan hoa tren bang?:
    def update(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())


    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,value=i)
    #import csv

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File",".csv"),("ALL File","*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
                print(mydata)
        self.fetchData(mydata)


    #export csv
    def exportCsv(self):
        # try:
            if len(mydata)<1:
                messagebox.showerror("Không có dữ liệu","Không có dữ liệu để xuất file",parent=self.root)
                return  False

            with open('Attendance_CSV/diemdanh.csv',mode="w",newline="",encoding="utf-8") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                exp_write.writerow((
                    'Mã Điểm danh', 'ID Sinh viên', 'Tên sinh viên', 'Lớp biên chế', 'Giờ vào', 'Giờ ra', 'Ngày', 'ID Buổi học', 'Trạng thái'
                    ))
                for i in mydata:
                    exp_write.writerow(i)

                messagebox.showinfo("Xuất Dữ Liệu","Dữ liệu của bạn đã được xuất đến "+os.path.basename('diemdanh.csv')+" thành công", parent=self.root)


    def get_cursor(self, event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_idsv.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_class.set(rows[3])
        self.var_atten_timein.set(rows[4])
        self.var_atten_timeout.set(rows[5])
        self.var_atten_date.set(rows[6])
        self.var_atten_attendance.set(rows[8])
        self.var_atten_lesson.set(rows[7])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_idsv.set("")
        self.var_atten_name.set("")
        self.var_atten_class.set("")
        self.var_atten_timein.set("")
        self.var_atten_timeout.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")
        self.var_atten_lesson.set("Lesson")
    def update_data(self):
        if self.var_atten_lesson.get()=="Lesson" or self.var_atten_attendance.get()=="Status" or self.var_atten_id.get()=="":
            messagebox.showerror("Error","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Bạn có muốn cập nhật bản ghi này không?",parent=self.root)
                if Update>0:
                    self.db.connect()
                    self.db.my_cursor.execute("update attendance set Student_id=%s,Name=%s,Class=%s,Time_in=%s,Time_out=%s,Date=%s,AttendanceStatus=%s,"
                                      "Lesson_id=%s where IdAuttendance=%s",(
                                            self.var_atten_idsv.get(),
                                            self.var_atten_name.get(),
                                            self.var_atten_class.get(),
                                            self.var_atten_timein.get(),
                                            self.var_atten_timeout.get(),
                                            self.var_atten_date.get(),
                                            self.var_atten_attendance.get(),
                                            self.var_atten_lesson.get(),

                                            self.var_atten_id.get()
                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Thành công","Cập nhật thông tin điểm danh thành công",parent=self.root)
                self.db.conn.commit()
                self.fetch_data()
                self.db.conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi",f"Due To:{str(es)}",parent=self.root)

    # Delete Function
    def delete_data(self):
            if self.var_atten_id.get() == "":
                messagebox.showerror("Lỗi", "Không được bỏ trống ID ", parent=self.root)
            else:
                try:
                    delete = messagebox.askyesno("Xoá bản ghi", "Bạn có muốn xóa bản ghi này ?", parent=self.root)
                    if delete > 0:
                        self.db.connect()
                        sql = "delete from attendance where IdAuttendance=%s"
                        val = (self.var_atten_id.get(),)
                        self.db.my_cursor.execute(sql, val)
                    else:
                        if not delete:
                            return
                    self.db.close()
                    messagebox.showinfo("Xóa", "Xóa bản ghi thành công", parent=self.root)
                    self.fetch_data()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self.root)
    def openImage(self):
        if self.var_atten_id == "":
            messagebox.showerror("Lỗi", " Vui lòng chọn ID để xem ảnh", parent=self.root)


        elif(self.var_atten_timein.get()=='None' ):
            if not os.path.exists("DiemDanhImage\ " + self.var_atten_id.get() +"Ra" +".jpg"):
                messagebox.showerror("Lỗi", "Không tìm thấy ảnh điểm danh", parent=self.root)
            else:
                img = cv2.imread("DiemDanhImage\ " + str(self.var_atten_id.get()) +"Ra"+ ".jpg")
                img = cv2.resize(img, (300, 300))
                cv2.imshow("Out of Class", img)
        elif(self.var_atten_timeout.get()=='None'):
            if not os.path.exists("DiemDanhImage\ " + self.var_atten_id.get() + ".jpg"):
                messagebox.showerror("Lỗi", "Không tìm thấy ảnh điểm danh", parent=self.root)
            else:
                img1=cv2.imread("DiemDanhImage\ " + str(self.var_atten_id.get()) + ".jpg")
                img1=cv2.resize(img1,(300,300))
                cv2.imshow("Into Class",img1)
        elif(self.var_atten_timein.get()!='None' and self.var_atten_timeout.get()!='None'):
            img = cv2.imread("DiemDanhImage\ " + str(self.var_atten_id.get()) + "Ra" + ".jpg")
            img = cv2.resize(img, (300, 300))
            img1 = cv2.imread("DiemDanhImage\ " + str(self.var_atten_id.get()) + ".jpg")
            img1 = cv2.resize(img1, (300, 300))
            Hori = np.concatenate((img, img1), axis=1)
            cv2.imshow("InAndOutClass", Hori)
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy ảnh điểm danh", parent=self.root)
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Lỗi !","Vui lòng nhập thông tin đầy đủ")

        else:
            try:
                #"ID Điểm Danh", "Ngày", "ID Sinh Viên"
                self.db.connect()
                if(self.var_com_search.get()=="ID Điểm Danh"):
                    self.var_com_search.set("IdAuttendance")
                elif(self.var_com_search.get()=="Ngày"):
                    self.var_com_search.set("Date")
                else:
                    if(self.var_com_search.get()=="ID Sinh Viên"):
                        self.var_com_search.set("Student_id")
                    elif(self.var_com_search.get()=="ID Buổi học"):
                        self.var_com_search.set("Lesson_id")
                mydata.clear()
                self.db.my_cursor.execute("select * from attendance where "+str(self.var_com_search.get())+" Like '%"+str(self.var_search.get())+"%'")
                data = self.db.my_cursor.fetchall()
                if(len(data)!=0):
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    for i in data:
                        self.AttendanceReportTable.insert("",END,values=i)
                        mydata.append(i)
                    messagebox.showinfo("Thông báo","Có "+str(len(data))+" bản ghi thỏa mãn điều kiện",parent=self.root)
                    self.db.conn.commit()
                else:
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                self.db.conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self.root)
    def today_data(self):
        try:
            # "ID Điểm Danh", "Ngày", "ID Sinh Viên"
            self.db.connect()
            mydata.clear()
            d1 = strftime("%d/%m/%Y")
            self.db.my_cursor.execute("select * from attendance where Date Like '%" + str(
                d1) + "%'")
            data = self.db.my_cursor.fetchall()
            if (len(data) != 0):

                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in data:
                    self.AttendanceReportTable.insert("", END, values=i)
                    mydata.append(i)
                messagebox.showinfo("Thông báo", "Có " + str(len(data)) + " bản ghi hôm nay",parent=self.root)
                self.db.conn.commit()
            else:
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                messagebox.showinfo("Thông báo", " Không có bản ghi nào trong hôm nay !",parent=self.root)
            self.db.conn.close()
        except Exception as es:
            messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self.root)

if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Attendance(root)
    root.mainloop()# cua so hien len