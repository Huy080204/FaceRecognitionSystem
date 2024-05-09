import mysql.connector

from DBConnection import DBConnection

class StudentDAO(DBConnection):
    def __init__(self):
        super().__init__()

    def get_next_id(self):
        self.connect()
        self.my_cursor.execute(
            "SELECT Student_id from student ORDER BY Student_id DESC limit 1")
        lastid = self.my_cursor.fetchone()
        self.close()
        return "1" if lastid == None else str(int(lastid[0]) + 1)
    
    def select(self):
        self.connect()
        self.my_cursor.execute("SELECT * FROM student")
        data = self.my_cursor.fetchall()
        self.close()
        return data


    def insert(self, id, dep, course, year, semester, name, div, roll, gender, date_of_birth, email, phone, address, is_image):
        self.connect()
        self.my_cursor.execute("INSERT INTO student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            id, dep, course, year, semester, name, div, roll, gender, date_of_birth, email, phone, address, is_image
        ))
        self.commit_and_close()

    def delete(self, id):
        self.connect()
        sql = "delete from student where Student_id=%s"
        val = (id,)
        print(val)
        self.my_cursor.execute(sql, val)
        self.commit_and_close()

    def update(self, dep, course, year, semester, name, div, roll, gender, date_of_birth, email, phone, address, is_image, id):
        self.connect()
        self.my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Class=%s,"
                                      "Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
            dep, course, year, semester, name, div, roll, gender, date_of_birth, email, phone, address, is_image, id))
        self.commit_and_close()

    def search(self, attribute, keyword):
        self.connect()
        self.my_cursor.execute(f"SELECT * FROM student WHERE {attribute} LIKE '{keyword}%'")
        data = self.my_cursor.fetchall()
        self.close()
        return data