from database.db_manager import DBManager

if __name__ == "__main__":
    db = DBManager()
    db.connect()
    db.close()
