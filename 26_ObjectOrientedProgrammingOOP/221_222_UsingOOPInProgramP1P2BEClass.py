# 13'01'' + 14'06''
# Fajlovi BEClass i FEClass su kopije 221_222... fajlova radi lakseg importa u cod

import sqlite3

class Database:
    
    def __init__(self, db):     # u drugim jezicima zove se konstruktor, izvrsava se pri pozivu klase!
        self.conn=sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn    integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()
        
    def __del__(self):
        self.conn.commit()


# connect()
# insert("Maca", "Anja jerak Glavan", 1963, 975436464)
# insert("Maca", "Antun Jerak", 1963, 975436464)
# delete(1)
# update(3,"Macaaa", "Anjaaa", 1991, 99555555)
# print(view())
# print(search(author="Antun Jerak"))

