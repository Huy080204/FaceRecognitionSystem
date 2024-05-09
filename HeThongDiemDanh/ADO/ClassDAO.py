import mysql.connector

from DBConnection import DBConnection

class ClassDAO(DBConnection):
    def __init__(self):
        super().__init__()

    def get_list_class(self):
        self.connect()
        self.my_cursor.execute("SELECT Class FROM class")
        ckclass = self.my_cursor.fetchall()
        list_class = []
        for chc in ckclass:
            list_class.append(str(chc[0]))
        return list_class
    
    def select(self):
        self.connect()
        self.my_cursor.execute("Select * from class")
        data = self.my_cursor.fetchall()
        self.close()
        return data

    def insert(self, id_class, name_class):
        self.connect()
        self.my_cursor.execute("insert into class values(%s,%s)", (
                    id_class,
                    name_class,
                ))
        self.commit_and_close()

    def delete(self, id):
        self.connect()
        sql = "delete from class where Class=%s"
        val = (id,)
        self.my_cursor.execute(sql, val)
        self.commit_and_close()

    def update(self, name_class, id_class):
        self.connect()
        self.my_cursor.execute("UPDATE class SET Name = %s WHERE Class = %s",
                               (name_class, id_class))
        self.commit_and_close()

    def search(self, attribute, keyword):
        self.connect()
        self.my_cursor.execute(f"SELECT * FROM class WHERE {attribute} LIKE '{keyword}%'")
        data = self.my_cursor.fetchall()
        self.close()
        return data

