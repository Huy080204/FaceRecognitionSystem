import mysql.connector

class DBConnection:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123456789'
        self.database = 'face_recognizer'
        self.port = '3306'

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            self.my_cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print("Error:", e)


    def commit_and_close(self):
        try:
            self.conn.commit()
            self.conn.close()
        except mysql.connector.Error as e:
            print("Error:", e)


    def close(self):
        try:
            self.conn.close()
        except mysql.connector.Error as e:
            print("Error:", e)