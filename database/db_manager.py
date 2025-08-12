import mysql.connector

class DBManager:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',          # kendi MySQL kullanıcı adını yaz (genelde 'root')
                password='94542148hS.',  # kurarken belirlediğin MySQL şifresini yaz
                database='state_education_db'
            )
            print("MySQL connection successful!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection = None

    def close(self):
        if self.connection:
            self.connection.close()
