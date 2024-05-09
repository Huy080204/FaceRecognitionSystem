from DBConnection import DBConnection

class TeacherDAO(DBConnection):
    def __init__(self):
        super().__init__()

    def get_id_by_email_and_password(self, email, password):
        self.connect()
        self.my_cursor.execute("select Teacher_id from teacher where Email=%s and Password=%s",(
                                    email, password
                                ))
        row = self.my_cursor.fetchone()
        self.close()
        return row
    
    def get_next_id(self):
        self.connect()
        self.my_cursor.execute(
            "SELECT Teacher_id from teacher ORDER BY Teacher_id DESC limit 1")
        lastid = self.my_cursor.fetchone()
        self.close()
        return "1" if lastid == None else str(int(lastid[0]) + 1)
    
    def select(self):
        self.connect()
        self.my_cursor.execute("SELECT * FROM teacher")
        data = self.my_cursor.fetchall()
        self.close()
        return data
    
    def insert(self, id, name, phone, email, password):
        self.connect()
        self.my_cursor.execute("INSERT INTO teacher values(%s,%s,%s,%s,%s)",(
            id, name, phone, email, password))
        self.commit_and_close()

    def delete(self, id):
        self.connect()
        sql = "delete from teacher where Teacher_id=%s"
        val = (id,)
        self.my_cursor.execute(sql, val)
        self.commit_and_close()

    def update(self, name, phone, email, password, id):
        self.connect()
        self.my_cursor.execute("update teacher set Name=%s,Phone=%s,Email=%s,Password=%s"
                                " where Teacher_id=%s",(
                                    name, phone, email, password, id))
        self.commit_and_close()

    def search(self, attribute, keyword):
        self.connect()
        self.my_cursor.execute(f"SELECT * FROM teacher WHERE {attribute} LIKE '{keyword}%'")
        data = self.my_cursor.fetchall()
        self.close()
        return data