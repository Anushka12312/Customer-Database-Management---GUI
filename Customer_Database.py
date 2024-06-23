import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Customer (Customer_ID INTEGER PRIMARY KEY, Customer_Name text,\
                   Customer_Email_ID text, Customer_City text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM Customer")
        row = self.cur.fetchall()
        return row

    def insert(self, Name, Email, City):
    # Check if the record already exists
        self.cur.execute("SELECT * FROM Customer WHERE Customer_Name = ? AND Customer_Email_ID = ? AND Customer_City = ?", (Name, Email, City))
        if self.cur.fetchone() is None:
            self.cur.execute("INSERT INTO Customer VALUES (NULL, ?, ?, ?)", (Name, Email, City))
            self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM Customer WHERE Customer_ID=?", (id,))
        self.conn.commit()

    def update(self, id, Name, Email, City):
        self.cur.execute("UPDATE Customer SET Customer_Name = ?, \
                         Customer_Email_ID = ?, Customer_City = ? WHERE Customer_ID = ?",
                         (Name, Email, City, id))
        self.conn.commit()

    def execute_query(self, sql_command):
        try:
            self.cur.execute(sql_command)
            rows = self.cur.fetchall()
            return rows
        except sqlite3.Error as e:
            raise e   

    def __del__(self):
        self.conn.close()




#db = Database('store.db')
#db.insert("Ritika Shah", "ritika.shah12@gmail.com", "Mumbai")
#db.insert("Megha R", "megha456.r@gmail.com", "Pune")
#db.insert("Aayush Singh", "aayush.singh@gmail.com", "Navi Mumbai")
#db.insert("Anuj Kumar", "anuj.kumar34@gmail.com", "Mumbai")
#db.insert("Bhumi Sinha", "bhumi.s567@gmail.com", "Navi Mumbai")
#db.insert("Nidhi Yadav", "nidhi.yadav@gmail.com", "Pune")
#db.insert("Yash Yadav", "yash.mehra@gmail.com", "Mumbai")